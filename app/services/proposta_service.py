from app.schemas.proposta import PropostaCreate, PropostaUpdate
from app.repositories.proposta_repository import PropostaRepository
from app.repositories.evento_repository import EventoRepository

class PropostaService:
    def __init__(self, repository: PropostaRepository, evento_repository: EventoRepository):
        self.repository = repository
        self.evento_repository = evento_repository

    def criar_proposta(self, dados: PropostaCreate):
        if dados.valor_decoracao < 0:
            raise ValueError ('O valor da decoração informado deve ser maior que 0.')

        if dados.valor_moveis < 0:
                raise ValueError ('O valor dos móveis informado deve ser maior que 0.')

        if dados.valor_adicionais < 0:
                raise ValueError ('O valor dos adicionais informado deve ser maior que 0.')

        if dados.valor_total <= 0:
            raise ValueError ('O valor total informado deve ser maior que 0.')


        evento = self.evento_repository.buscar_evento_por_id(dados.id_evento)

        if evento is None:
             raise ValueError('Não foi possível loclaizar o evento.')

        return self.repository.criar_proposta(dados)

    def buscar_proposta_por_id(self, id_proposta: int):
        proposta = self.repository.buscar_proposta_por_id(id_proposta)

        if proposta is None:
             raise ValueError('Não foi possível localizar nenhuma proposta.')

        return proposta
    

    def buscar_propostas_por_evento(self, id_evento: int):
        return self.repository.buscar_propostas_por_evento(id_evento)
    
    def buscar_propostas_por_status(self, status: str):
        return self.repository.buscar_propostas_por_status(status)

    def buscar_proposta_por_evento_e_versao(self, id_evento: int, versao: int):
       return self.repository.buscar_proposta_por_evento_e_versao(id_evento, versao)

    def listar_propostas(self):
        return self.repository.listar_propostas()
    

    def atualizar_proposta(self, id_proposta: int, dados: PropostaUpdate):
        proposta = self.repository.buscar_proposta_por_id(id_proposta)

        if proposta is None:
             raise ValueError('Não foi possível localizar nenhuma proposta.')


        if dados.id_evento is not None:
            evento = self.evento_repository.buscar_evento_por_id(dados.id_evento)

            if evento is None:
                raise ValueError('Não foi possível localizar o evento.')

        if proposta.status != 'pendente':
            raise ValueError('Não é possível alterar uma proposta finalizada.')


        return self.repository.atualizar_proposta(id_proposta, dados)

    def atualizar_status_proposta(self, id_proposta: int, status: str):
        proposta = self.repository.buscar_proposta_por_id(id_proposta)

        if proposta is None:
             raise ValueError('Não foi possível localizar nenhuma proposta.')

        transicoes = {'pendente': ['aceito', 'recusado', 'cancelado'], 
                      'aceito': [], 
                      'recusado': [],
                      'cancelado': []}
            
        if status not in transicoes[proposta.status]:
            raise ValueError('Transição de status não permitida')
        
        return self.repository.atualizar_status_proposta(id_proposta, status)