from fastapi import HTTPException, status, Depends
from app.dependencies.jwt_bearer import oauth2_scheme
from app.dependencies.security import decode_access_token
from app.models.user import User


async def get_current_user(token: str = Depends(oauth2_scheme)) -> User:
    
    # Verificação do token
    payload = decode_access_token(token)
    if payload is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # Extração do user_id
    user_id = payload.get("sub")
    if not user_id:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token payload",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # Busca pelo usuário
    user = await User.get_or_none(id=user_id)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # Verificação de usuário ativo
    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Inactive user",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    return user