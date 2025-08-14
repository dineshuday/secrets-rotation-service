from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer
import os
import jwt

security = HTTPBearer()
SECRET_KEY = os.getenv("JWT_SECRET", "demo-secret")

def verify_token(credentials=Depends(security)):
    try:
        jwt.decode(credentials.credentials, SECRET_KEY, algorithms=["HS256"])
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")