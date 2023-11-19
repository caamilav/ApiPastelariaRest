from sqlalchemy import CHAR, VARCHAR, Column, Date, Integer
import db

class ClienteDB(db.Base):
    __tablename__ = "tb_cliente"
    id_cliente = Column(Integer, primary_key=True, autoincrement=True, index=True)
    nome = Column(VARCHAR(100), nullable=False)
    cpf = Column(CHAR(11), nullable=False)
    telefone = Column(CHAR(11), nullable=False)
    compra_fiado = Column(Integer, nullable=False)
    dia_fiado = Column(VARCHAR(100), nullable=True)
    senha = Column(VARCHAR(200), nullable=False)
    
    def __init__(self, id_cliente, nome, cpf, telefone,
                 compra_fiado, dia_fiado, senha):
        self.id_cliente = id_cliente
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.compra_fiado = compra_fiado
        self.dia_fiado =  dia_fiado
        self.senha = senha
