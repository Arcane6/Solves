# app/api/v1/auth.py
from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException, status, Request
from fastapi.security import OAuth2PasswordRequestForm

from app.core.config import settings
from app.dependencies.security import create_access_token, decode_access_token
from app.schemas.token import TokenSchema
from app.services.user_service import UserService
from app.services.user_session_service import SessionService
from app.dependencies.rate_limiter import limiter
from app.core.logger import logger
from app.services.log_service import AuditService


router = APIRouter(prefix="/auth", tags=["auth"])

# Rota para login
@router.post("/login", response_model=TokenSchema)
@limiter.limit("5/minute")  
async def login(form_data: OAuth2PasswordRequestForm = Depends(),request: Request = None):
    # Verifica se o usuário existe e se a senha está correta
    user = await UserService.get_user_by_email(form_data.username)
    if not user or not UserService.verify_password(form_data.password, user.hashed_password):
        logger.warning(f"Falha de login para {form_data.username}")
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Credenciais inválidas")

    access_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    refresh_expires = timedelta(days=settings.REFRESH_TOKEN_EXPIRE_DAYS)

    access_token = create_access_token(
        {"sub": str(user.id)}, expires_delta=access_expires
    )
    refresh_token = create_access_token(
        {"sub": str(user.id), "type": "refresh"}, expires_delta=refresh_expires
    )

    await SessionService.create_session(
        user=user,
        session_token=access_token,
        refresh_token=refresh_token,
        ip=request.client.host if request.client else "unknown",
        user_agent=request.headers.get("User-Agent", "")
    )


    logger.info(f"Login bem-sucedido para {user.email}")
    await AuditService.log(user.id, "login", {"ip": request.client.host})

    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer"
    }

# Endpoint de refresh
@router.post("/refresh", response_model=TokenSchema)
async def refresh_token(token: str):
    payload = decode_access_token(token)
    if not payload or payload.get("type") != "refresh":
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token inválido")

    user_id = payload["sub"]
    access_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    refresh_expires = timedelta(days=settings.REFRESH_TOKEN_EXPIRE_DAYS)

    new_access = create_access_token({"sub": user_id}, expires_delta=access_expires)
    new_refresh = create_access_token({"sub": user_id, "type": "refresh"}, expires_delta=refresh_expires)

    return {
        "access_token": new_access,
        "refresh_token": new_refresh,
        "token_type": "bearer"
    }


# Endpoint de logout
@router.post("/logout")
async def logout(request: Request):
    token = request.headers.get("Authorization", "").replace("Bearer ", "")
    await SessionService.delete_session(token)
    logger.info(f"Logout de {token.user.email}")
    return {"detail": "Sessão encerrada com sucesso"}
