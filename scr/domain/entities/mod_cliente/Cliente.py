import datetime
from pydantic import BaseModel

class Cliente(BaseModel):
    id_cliente: int = None
    nome: str
    cpf: str
    telefone: str
    compra_fiado: int
    dia_fiado: datetime.date = None
    senha: str  