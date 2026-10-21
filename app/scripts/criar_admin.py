from getpass import getpass

from sqlalchemy import select

from app.core.database import SessionLocal
from app.models.usuario import Usuario
from app.schemas.usuario import UsuarioCreate
from app.repositories.usuario_repository import UsuarioRepository
from app.services.usuario_service import UsuarioService

def criar_admin_inicial():
    db = SessionLocal()

    try:
        usuario_existente = db.execute(select(Usuario.id_usuario).limit(1)).first()

        if usuario_existente is not None:
            print("Já existe um usuário cadastrado. Inicialização bloqueada.")
            return

        nome = input("Nome do administrador: ").strip()
        email = input("E-mail: ").strip()
        senha = getpass("Senha: ")
        confirmacao = getpass("Confirme a senha: ")

        if senha != confirmacao:
            print("As senhas não coincidem.")
            return

        if not 8 <= len(senha) <= 100:
            print("A senha deve conter entre 8 e 100 caracteres.")
            return

        dados = UsuarioCreate(nome=nome, email=email, senha=senha, perfil='admin')

        repository = UsuarioRepository(db)
        service = UsuarioService(repository)

        usuario = service.criar_usuario(dados)

        print(f'Administrador criado com sucesso: ID = {usuario.id_usuario}')

    except ValueError as erro:
        print(f"Erro: {erro}")

    finally:
        db.close()

if __name__ == '__main__':
    criar_admin_inicial()