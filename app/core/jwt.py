import jwt
import os

from datetime import datetime, timedelta, timezone
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.environ["JWT_SECRET_KEY"]
ALGORITHM = os.getenv("JWT_ALGORITHM", "HS256")
EXPIRE_MINUTES = int(os.getenv("JWT_EXPIRE_MINUTES", "30"))


def criar_token_acesso(id_usuario: int) -> str:
    expiracao = datetime.now(timezone.utc)+timedelta(minutes=EXPIRE_MINUTES)

    payload = {
        'sub': str(id_usuario),
        'exp': expiracao
    }

    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM) 

    return token

def verificar_token(token: str) -> int:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithm=[ALGORITHM], option={'require': ["sub", "exp"]})

        id_usuario = int(payload['sub'])

        return id_usuario

    except(jwt.InvalidTokenError, ValueError, TypeError):
        raise ValueError('Token inválido ou expirado.')
