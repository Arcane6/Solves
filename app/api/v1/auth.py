from fastapi import APIRouter, Depends, HTTPException, status, Request
from fastapi.security import OAuth2PasswordRequestForm
from app.schemas.token import TokenSchema
from app.services.user_service import UserService
from app.services.user_session_service import SessionService
from app.dependencies.security import create_access_token
from app.schemas.user import UserRead

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/login", response_model=TokenSchema)
async def login(form_data: OAuth2PasswordRequestForm = Depends(), request: Request = None):
    user = await UserService.get_user_by_email(form_data.username)
    if not user or not UserService.verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Credenciais inválidas")
    
    token = create_access_token({"sub": str(user.id)})
    await SessionService.create_session(
        user=user,
        session_token=token,
        ip=request.client.host if request.client else "unknown",
        user_agent=request.headers.get("User-Agent", "")
    )
    return {"access_token": token, "token_type": "bearer"}


@router.post("/logout")
async def logout(request: Request):
    token = request.headers.get("Authorization", "").replace("Bearer ", "")
    await SessionService.delete_session(token)
    return {"detail": "Sessão encerrada com sucesso"}
