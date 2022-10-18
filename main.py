from fastapi import FastAPI
from Routes.usuarioRoute import router as UsuarioRouter
from Routes.autenticacaoRoute import router as autenticacaoRoute

app = FastAPI()

app.include_router(UsuarioRouter, tags=['Usuário'], prefix='/api/usuario')
app.include_router(autenticacaoRoute, tags=['Autenticação'], prefix='/api/auth')

@app.get('/api/health', tags=['health'])
async def healt():
    return {
        'status': 'ok'
    }

