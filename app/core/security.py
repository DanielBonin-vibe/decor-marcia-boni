from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError, VerificationError

ph = PasswordHasher()

def gerar_hash(senha: str) -> str:
    return ph.hash(senha)

def verificar_senha(senha: str, senha_hash: str) -> bool:
    try:
        return ph.verify(senha_hash, senha)

    except (VerifyMismatchError, VerificationError):
        return False