from fastapi import FastAPI
from app.routers.auth_router import router as auth_router
from app.routers.usuario_router import router as usuario_router
from app.routers.cliente_router import router as cliente_router
from app.routers.contrato_router import router as contrato_router
from app.routers.documento_router import router as documento_router
from app.routers.evento_router import router as evento_router
from app.routers.item_proposta_router import router as item_proposta_router
from app.routers.pagamento_router import router as pagamento_router
from app.routers.parcela_router import router as parcela_router
from app.routers.proposta_router import router as proposta_router
from app.routers.recibo_router import router as recibo_router
from app.pages.auth_pages import router as auth_pages_router

app = FastAPI(title='Decor Márcia Boni', 
    description="Sistema de gestão de eventos e automação documental",
    version='1.0.0'          
    )

@app.get('/')
def inicio():
    return {'mensagem': 'API Decor Márcia Boni funcionando!'}

app.include_router(auth_router)
app.include_router(usuario_router)
app.include_router(cliente_router)
app.include_router(contrato_router)
app.include_router(documento_router)
app.include_router(evento_router)
app.include_router(item_proposta_router)
app.include_router(pagamento_router)
app.include_router(parcela_router)
app.include_router(proposta_router)
app.include_router(recibo_router)
app.include_router(auth_pages_router)