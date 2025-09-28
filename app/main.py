from fastapi import FastAPI 
from fastapi.responses import RedirectResponse
from .db.database_conn import Base , engine
from .api.user_auth import user_Auth_route
from app.jwt_config import register_jwt_exception_handler
app = FastAPI(
    title= "user Service micro"
)

app.include_router(user_Auth_route)

@app.on_event("startup")
async def get_conn_with_db():
    Base.metadata.create_all(engine)

register_jwt_exception_handler(app)


@app.get("/" , include_in_schema=False)
def go_to_docs():
  return  RedirectResponse(url="/docs")