# jwt_config.py
from fastapi import Request 
from fastapi.responses import JSONResponse 
from fastapi_jwt_auth import AuthJWT
from fastapi_jwt_auth.exceptions import AuthJWTException
from pydantic import BaseModel

class Settings(BaseModel):
    authjwt_secret_key: str = "0980s89028908209nc093ur82098r0c2938r02830c802380vnweoehfwiohfwiury923"
    authjwt_token_location: set = {"headers", "cookies"} 
    authjwt_cookie_csrf_protect: bool = False
    authjwt_access_token_expires: int = 60 * 1500
    authjwt_refresh_token_expires: int = 60 * 60 * 24 * 30  

@AuthJWT.load_config
def get_config():
    return Settings()

def register_jwt_exception_handler(app):
    @app.exception_handler(AuthJWTException)
    async def authjwt_exception_handler(request: Request, exc):
        status_code = getattr(exc, "status_code", 401)
        message = getattr(exc, "message", "Access token required")
        return JSONResponse(
            status_code=status_code,
            content={"detail": message}
        )
