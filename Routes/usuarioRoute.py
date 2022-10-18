from fastapi import APIRouter, Body, HTTPException

from Models.usuarioModel import usuarioCriarModel
from services.usuarioService import registrar_ususario


router = APIRouter()

@router.post('/', response_description='Rota para criar um usuário')
async def rota_criar_usuario(usuario: usuarioCriarModel = Body(...)):
    resultado = await registrar_ususario(usuario)

    if not resultado['status'] == 201:
        raise HTTPException(status_code=resultado['status'],detail=resultado['mensagem'])

    return resultado