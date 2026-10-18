from datetime import datetime, timedelta, timezone
import os
import secrets

import jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer


def _required_env(name: str) -> str:
    value = os.environ.get(name)
    if not value or not value.strip():
        raise RuntimeError(f"{name} must be set to a non-empty value")
    return value


# No default credentials: configure these privately before starting the API.
SECRET_KEY = _required_env("SECRET_KEY")
if len(SECRET_KEY.encode("utf-8")) < 32:
    raise RuntimeError("SECRET_KEY must contain at least 32 bytes")
DEMO_USERNAME = _required_env("DEMO_USERNAME")
DEMO_PASSWORD = _required_env("DEMO_PASSWORD")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")


def verify_login(username: str, password: str) -> bool:
    username_matches = secrets.compare_digest(
        username.encode("utf-8"), DEMO_USERNAME.encode("utf-8")
    )
    password_matches = secrets.compare_digest(
        password.encode("utf-8"), DEMO_PASSWORD.encode("utf-8")
    )
    return username_matches and password_matches


def create_access_token(subject: str) -> str:
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    payload = {"sub": subject, "exp": expire}
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)


def get_current_user(token: str = Depends(oauth2_scheme)) -> str:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid or missing token",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except jwt.PyJWTError as error:
        raise credentials_exception from error

    username = payload.get("sub")
    if not username:
        raise credentials_exception

    return username