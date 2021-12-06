from pydantic import BaseModel, EmailStr, SecretStr, validator

from .models import User

class UserLoginSchema(BaseModel):
    email: EmailStr
    password: SecretStr


class UserSignupSchema(BaseModel):
    email: EmailStr
    password: SecretStr
    password_confirm: SecretStr
        
    
    @validator("email")
    def email_available(cls, v, values, **kwargs):
        q = User.objects.filter(email=v)
        if q.count() != 0:
            raise ValueError("Email is not available")
        return v
        
    @validator("password_confirm")
    def passwords_match(cls, v, values, **kwargs):
        password = values.get('password')
        password_confirm = v
        if password != password_confirm:
            raise ValueError("Passwords do not match")
        return v