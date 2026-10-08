from app.schemas.cliente import ClienteCreate, ClienteUpdate
from app.repositories.cliente_repository import ClienteRepository

class ClienteService:
    def __init__(self, repository: ClienteRepository):
        self.repository = repository

    def criar_cliente(self, dados: ClienteCreate):
        cliente_cpf = self.repository.buscar_cliente_por_cpf(dados.cpf)

        if cliente_cpf is not None:
            raise ValueError('CPF já cadastrado.')
        

        email_normalizado = str(dados.email).strip().lower()

        cliente_email = self.repository.buscar_cliente_por_email(email_normalizado)

        if cliente_email is not None:
            raise ValueError('Email já cadastrado.')


        cliente_telefone = self.repository.buscar_cliente_por_telefone(dados.telefone)

        if cliente_telefone is not None:
            raise ValueError('Telefone já cadastrado.')
        

        dados = dados.model_copy(update={'email': email_normalizado})

        return self.repository.criar_cliente(dados)


    def buscar_cliente_por_id(self, id_cliente: int):
        cliente = self.repository.buscar_cliente_por_id(id_cliente)

        if cliente is None:
            raise ValueError('Cliente não encontrado.')

        return cliente

    def buscar_cliente_por_cpf(self, cpf: str):
        cliente = self.repository.buscar_cliente_por_cpf(cpf)

        if cliente is None:
            raise ValueError('Cliente não encontrado.')

        return cliente

    def buscar_cliente_por_email(self, email: str):
        cliente = self.repository.buscar_cliente_por_email(email)

        if cliente is None:
            raise ValueError('Cliente não encontrado.')

        return cliente

    def buscar_cliente_por_telefone(self, telefone: str):
        cliente = self.repository.buscar_cliente_por_telefone(telefone)

        if cliente is None:
            raise ValueError('Cliente não encontrado.')

        return cliente

    def listar_clientes(self):
        cliente = self.repository.listar_clientes()

        if cliente is []:
            raise ValueError('Cliente não encontrado')

        return cliente

    def atualizar_cliente(self, cpf: str, dados: ClienteUpdate):
        cliente = self.repository.buscar_cliente_por_cpf(cpf)

        if cliente is None:
            raise ValueError('Cliente não encontrado.')
        

        if dados.cpf  is not None:
            cpf_cliente = self.repository.buscar_cliente_por_cpf(dados.cpf)

            if cpf_cliente is not None and cpf_cliente.id_cliente != cliente.id_cliente:
                raise ValueError('O CPF infromado já está vinculado a outro cliente.')


        if dados.telefone is not None:
            telefone_cliente = self.repository.buscar_cliente_por_telefone(dados.telefone)

            if telefone_cliente is not None and telefone_cliente.id_cliente != cliente.id_cliente:
                raise ValueError('O telefone informado já está vinculado a outro cliente.')

        
        if dados.email is not None:
            email_normalizado = str(dados.email).strip().lower()

            cliente_email = self.repository.buscar_cliente_por_email(email_normalizado)

            if cliente_email is not None and cliente_email.id_cliente != cliente.id_cliente:
                raise ValueError('Email já cadastrado por outro cliente.')

            dados = dados.model_copy(update={"email": email_normalizado})


        return self.repository.atualizar_cliente(cpf, dados)

    def desativar_cliente(self, cpf: str):
        cliente = self.repository.buscar_cliente_por_cpf(cpf)

        if cliente is None:
            raise ValueError('Cliente não encontrado.')

        return self.repository.desativar_cliente(cpf)

    def reativar_cliente(self, cpf: str):
        cliente = self.repository.buscar_cliente_por_cpf(cpf)

        if cliente is None:
            raise ValueError('Cliente não encontrado.')

        return self.repository.reativar_cliente(cpf)