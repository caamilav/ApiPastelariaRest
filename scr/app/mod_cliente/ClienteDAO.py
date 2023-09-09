from fastapi import APIRouter
from domain.entities.mod_cliente.Cliente import Cliente
from infra.orm.mod_cliente.ClienteModel import ClienteDB
import db

router = APIRouter()

# Criar os endpoints de Cliente: GET, POST, PUT, DELETE

@router.get("/cliente/", tags=["Cliente"])
def get_cliente():
   try:
       session = db.Session()
       dados = session.query(ClienteDB).all()
       
       if len(dados) == 0:
           return {"Nenhum registro encontrado"}, 200
          
       return dados, 200
   except Exception as ex:
       return {"erro": str(ex)}, 400
   finally:
       session.close()

@router.get("/cliente/{id}", tags=["Cliente"])
def get_cliente(id: int):
    try:
        session = db.Session()
        dados = session.query(ClienteDB).filter(ClienteDB.id_cliente == id).first()
        return dados, 200
    except Exception as ex:
        return {"erro": str(ex)}, 400
    finally:
        session.close()
    
@router.post("/cliente/", tags=["Cliente"])
def post_cliente(c: Cliente):
    try:
        session = db.Session()
        dados = ClienteDB(None, c.nome, c.cpf, c.telefone, c.compra_fiado, c.dia_fiado, c.senha)
        session.add(dados)
        session.commit()
        return {"id", dados.id_cliente}, 200
    except Exception as ex:
        session.rollback()
        return {"erro": str(ex)}, 400
    finally:
        session.close()
        

@router.put("/cliente/{id}", tags=["Cliente"])
def put_cliente(id: int, c: Cliente):
    try:
        session = db.Session()
        
        dados = session.query(ClienteDB).filter(ClienteDB.id_cliente == id).one()
        dados.nome = c.nome
        dados.cpf = c.cpf
        dados.telefone = c.telefone
        dados.compra_fiado = c.compra_fiado
        dados.dia_fiado = c.dia_fiado
        dados.senha = c.senha
    
        session.add(dados)
        session.commit()      
        return {"id": dados.id_cliente}, 200   
    except Exception as ex:
        session.rollback()
        return {"erro": str(ex)}, 400
    finally:
        session.close()
        

@router.delete("/cliente/{id}", tags=["Cliente"])
def delete_cliente(id: int):
    try:
        session = db.Session()
        dados = session.query(ClienteDB).filter(ClienteDB.id_cliente == id).one()
        session.delete(dados)
        session.commit()
        return {"id": dados.id_cliente}, 200     
    except Exception as ex:
        session.rollback()
        return {"erro": str(ex)}, 400
    finally:
        session.close()
