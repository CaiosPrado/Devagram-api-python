import time
import jwt
from decouple import config

from Models.usuarioModel import usuarioLoginModel
from repositories.usuarioRepository import buscar_usuario_por_email
from utils.authUtil import verificar_senha

JWT_SECRET = config('JWT_SECRET')

def gerar_token_jwt(usuario_id: str) -> str:
    payload = {
        'usuario_id': usuario_id,
        'tempo_expiração': time.time() + 600
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm='HS256')

    return token

def decodificar_token_jwt(token: str):
    try:
        token_decodificado = jwt.decode(token, JWT_SECRET, algorithms=['HS256'])

        if token_decodificado['tempo_expiração'] >= time.time():
            return token_decodificado
        else:
            return None
    except Exception as erro:
        print(erro)
        return {
            'mensagem': 'Erro interno no servidor',
            'dados': str(erro),
            'status': 500
        }

async def login_service(usuario: usuarioLoginModel):
    usuario_encontrado = await buscar_usuario_por_email(usuario.email)

    if not usuario_encontrado:
        return{
            'mensagem': 'Email ou senha incorreto.',
            'dados': '',
            'status': 401
        }
    else:
        if verificar_senha(usuario.senha, usuario_encontrado['senha']):

            return {
                'mensagem': 'Login realizado com sucesso',
                'dados': usuario_encontrado,
                'status': 200
            }
        else:
            return{
                'mensagem': 'Email ou senha incorreto.',
                'dados': '',
                'status': 401
            }

