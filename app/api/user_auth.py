from fastapi import APIRouter , Depends , HTTPException
from ..schemas.userSchemas import UserSchema ,UserLoginSchemaResponse , UserRegisterSchemaResponse
from ..db.database_conn import get_db
from sqlalchemy.orm import Session 
from ..db.models import User
from fastapi_jwt_auth import AuthJWT
from ..core.rabbitmq import send_message
from ..utils.hash_password import  Verify_password ,Hash_password
user_Auth_route = APIRouter(
    tags=["Auth"],
    prefix="/api"
)



@user_Auth_route.post("/register" , response_model=UserRegisterSchemaResponse)
def Register(data : UserSchema , db:Session = Depends(get_db)):
   user =db.query(User).filter(data.email == User.email).first()
   if user:
      raise HTTPException(status_code=404 , detail=("user already existed with this email"))
   if not data.email or not data.password:
      raise HTTPException(status_code=400 , detail="please enter both email and password")
   hashed_password = Hash_password(data.password)
   new_user = User(email=data.email , password= hashed_password)

   db.add(new_user)
   db.commit()
   db.refresh(new_user)
   return new_user



@user_Auth_route.post("/login" , response_model=UserLoginSchemaResponse)
def login(data:UserSchema , db:Session=Depends(get_db) , Authorize:AuthJWT=Depends()):
   user =db.query(User).filter(data.email == User.email).first()
   if not user:
      raise HTTPException(status_code=404 , detail=("user now found with email address"))
   correct_pass = Verify_password(data.password ,user.password)
   if not correct_pass:
      raise HTTPException(status_code=404 , detail=("wrong Credentials"))
   
   access_token =Authorize.create_access_token(subject=str(user.id))
   refresh_token= Authorize.create_refresh_token(subject=str(user.id))
   
   send_message("user_login_queue", {
        "id": str(user.id),
        "email": user.email,
        "status": user.status,
        "event": "user_logged_in"
    })
   return {
      "id": user.id,
      "email":user.email,
      "status": user.status,
      "created_at": user.created_at,
      "access_token" : access_token,
      "refresh_token" : refresh_token
   }


   
   

   
        

