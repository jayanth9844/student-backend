from datetime import datetime,timedelta,timezone
from jose import jwt,JWTError
from app.core.config import Settings
def create_token(data :dict , expire_minutes = 30):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=expire_minutes)
    to_encode.update({"exp":expire})
    return jwt.encode(
        to_encode,
        Settings.JWT_SECRET_KEY,
        algorithm=Settings.JWT_ALGORITH
    )


def verify_token(token:str):
    try:
        payload = jwt.decode(
            token,
            key = Settings.JWT_SECRET_KEY,
            algorithms=[Settings.JWT_ALGORITH]
        )
    except JWTError:
        return None