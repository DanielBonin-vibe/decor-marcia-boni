from app.schemas.usuario import UsuarioCreate, UsuarioUpdate
from app.repositories.usuario_repository import UsuarioRepository
from app.security.hash import gerar_hash

class UsuarioService:
    def __init__(self, repository: UsuarioRepository):
        self.repository = repository

    def criar_usuario(self, dados: UsuarioCreate):
        usuario_email = self.repository.buscar_usuario_por_email(dados.email)

        if usuario_email is not None:
            raise ValueError('O email informado já está vinculado a um usuário.')

        senha_hash = gerar_hash(dados.senha)

        return self.repository.criar_usuario(dados, senha_hash)

    def buscar_usuario_por_id(self, id_usuario: int):
        usuario = self.repository.buscar_usuario_por_id(id_usuario)

        if usuario is None:
            raise ValueError('Não foi possível localizar nenhum usuário.')

        return usuario

    def buscar_usuario_por_email(self, email: str):
        usuario = self.repository.buscar_usuario_por_email(email)

        if usuario is None:
            raise ValueError('Não foi possível localizar nenhum usuário.')

        return usuario

    def listar_usuarios(self):
        return self.repository.listar_usuarios()
    
    def atualizar_usuario(self, id_usuario: int, dados: UsuarioUpdate):
        usuario = self.repository.buscar_usuario_por_id(id_usuario)

        if usuario is None:
            raise ValueError('Não foi possível localizar nenhum usuário.')

        return self.repository.atualizar_usuario(id_usuario, dados)

    def atualizar_senha(self, id_usuario: int, senha_hash: str):
        usuario = self.repository.buscar_usuario_por_id(id_usuario)

        if usuario is None:
            raise ValueError('Não foi possível localizar nenhum usuário.')

        return self.repository.atualizar_senha(id_usuario, senha_hash)

    def atualizar_perfil(self, id_usuario: int, perfil: str):
        usuario = self.repository.buscar_usuario_por_id(id_usuario)

        if usuario is None:
            raise ValueError('Não foi possível localizar nenhum usuário.')

        return self.repository.atualizar_perfil(id_usuario, perfil)

    def desativar_usuario(self, id_usuario: int):
        usuario = self.repository.buscar_usuario_por_id(id_usuario)

        if usuario is None:
            raise ValueError('Não foi possível localizar nenhum usuário.')

        return self.repository.desativar_usuario(id_usuario)

    def reativar_usuario(self, id_usuario: int):
        usuario = self.repository.buscar_usuario_por_id(id_usuario)

        if usuario is None:
            raise ValueError('Não foi possível localizar nenhum usuário.')

        return self.repository.reativar_usuario(id_usuario)