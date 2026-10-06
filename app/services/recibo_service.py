from app.schemas.recibo import ReciboCreate, ReciboUpdate
from app.repositories.recibo_repository import ReciboRepository

class ReciboService:
    def __init__(self, repository: ReciboRepository):
        self.repository = repository

    def criar_recibo(self, dados: ReciboCreate):

        
        return