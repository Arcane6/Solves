from starlette.middleware.base import BaseHTTPMiddleware
from fastapi.requests import Request
from jose import JWTError
from app.dependencies.security import decode_access_token
from app.models.user import User



class AuthMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        token = self._extract_token_from_header(request)

        if token:
            try:
                payload = decode_access_token(token)
                user_id = payload.get("user_id") if payload else None

                if user_id:
                    user = User.get_or_none(id=user_id)

                    if user and user.is_active:
                        request.state.user = user
                    else:
                        request.state.user = None
                
                else:
                    request.state.user = None
            
            except JWTError:
                request.state.user = None
        else:
            request.state.user = None
        

        response = await call_next(request)
        return response
    

    def _extract_token_from_header(self, request: Request) -> str | None:
        auth_header = request.headers.get("Authorization")

        if auth_header and auth_header.startswith("Bearer "):
            return auth_header.split(" ")[1]
        return None