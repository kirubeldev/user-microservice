
from passlib.context import CryptContext



context = CryptContext(schemes=["bcrypt"] , deprecated="auto")

def Hash_password(password : str):
   return context.hash(password)



def Verify_password(password: str , hasedpassword : str):
  return context.verify(password , hasedpassword)
