from Models.usuarioModel import usuarioCriarModel
from repositories.usuarioRepository import (
    criar_usuario,
    buscar_usuario_por_email,
    listar_usuarios,
    atualizar_usuario,
    deletar_usuario
)

async def registrar_ususario(ususario: usuarioCriarModel):
    try:
        ususario_encontrado = await buscar_usuario_por_email(ususario.email)

        if ususario_encontrado:
            return {
                'mensagem': f'E-mail {ususario.email} já cadastrado ',
                'dados': '',
                'status': 400
            }
        else:
            novo_usuario = await criar_usuario(ususario)
            return {
                'mensagem': 'Usuário cadastrado com sucesso',
                'dados': novo_usuario,
                'status': 201
            }
    except Exception as error:
        return {
            'mensagem': 'Erro interno no servidor',
            'dados': str(error),
            'status': 500
        }