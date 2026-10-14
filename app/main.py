from fastapi import FastAPI
from app.routers.auth_router import router as auth_router
from app.routers.usuario_router import router as usuario_router

app = FastAPI(title='Decor Márcia Boni', 
    description="Sistema de gestão de eventos e automação documental",
    version='1.0.0'          
    )

@app.get('/')
def inicio():
    return {'mensagem': 'API Decor Márcia Boni funcionando!'}

app.include_router(auth_router)
app.include_router(usuario_router)