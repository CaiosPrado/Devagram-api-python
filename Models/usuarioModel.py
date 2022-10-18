from pydantic import BaseModel, Field, EmailStr

class usuarioModel(BaseModel):
    id: str = Field(...)
    nome : str = Field(...)
    email: EmailStr = Field(...)
    senha: str = Field(...)
    foto: str = Field(...)

    class config:
        schema_extra = {
            'usuário': {
                'nome': 'Fulano de tal',
                'email': 'fulano@gmail.com',
                'senha': 'seNha123',
                'foto': 'fulano.png'
            }
        }

class usuarioCriarModel(BaseModel):
    nome : str = Field(...)
    email: EmailStr = Field(...)
    senha: str = Field(...)
    foto: str = Field(...)

    class config:
        schema_extra = {
            'usuário': {
                'nome': 'Fulano de tal',
                'email': 'fulano@gmail.com',
                'senha': 'seNha123',
                'foto': 'fulano.png'
            }
        }

class usuarioLoginModel(BaseModel):
    email: EmailStr = Field(...)
    senha: str = Field(...)

    class config:
        schema_extra = {
            'usuário': {
                'email':'fulano@gmail.com',
                'senha':'seNha123'
            }
        }