import os
import jwt
from typing import List
from dotenv import load_dotenv
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer
from typing import Dict, Any

from auth.jwt import JWT

# Load the env variables
load_dotenv()

# Set up the secret and algorithm
SECRET_KEY = os.getenv("AUTH_SECRET")
ALGORITHM = os.getenv("AUTH_ALGORITHM")

# Define a reusable security scheme
security = HTTPBearer()

def decode_jwt(token: str) -> JWT:
    try:
        # Decode the JWT
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        jwt_user = JWT(payload.get("sub"), payload.get("roles"))
        return jwt_user
    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token has expired",
        )
    except jwt.InvalidTokenError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
        )
    
# Dependency that does Role-checking
def check_role(allowed_roles: List[str]):
    def role_checker(current_user: JWT = Depends(get_current_user)):
        roles = current_user.roles
        if not any(role in roles for role in allowed_roles):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="You do not have permission to perform this action.",
            )
        return current_user
    return role_checker

# Dependency that verifies and decodes JWT
def get_current_user(token: str = Depends(security)) -> JWT:
    return decode_jwt(token.credentials)
