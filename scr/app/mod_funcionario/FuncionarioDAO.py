from fastapi import APIRouter, Depends
from domain.entities.mod_funcionario.Funcionario import Funcionario
from infra.orm.mod_funcionario.FuncionarioModel import FuncionarioDB
import db
import security

router = APIRouter(dependencies=[Depends(security.verify_token), Depends(security.verify_key)])

# Criar as rotas/endpoints: GET, POST, PUT, DELETE

@router.get("/funcionario/", tags=["Funcionário"])
def get_funcionario():
    try: 
        session = db.Session()
        dados = session.query(FuncionarioDB).all()
    
        return dados, 200
    except Exception as ex:
        return {"erro": str(ex)}, 400
    finally: 
        session.close()

@router.get("/funcionario/{id}", tags=["Funcionário"])
def get_funcionario(id: int):
    try:
        session = db.Session()
        dados = session.query(FuncionarioDB).filter(FuncionarioDB.id_funcionario == id).one()
        return dados, 200
    except Exception as ex:
        return {"erro": str(ex)}, 400
    finally:
        session.close()


@router.post("/funcionario/", tags=["Funcionário"])
def post_funcionario(f: Funcionario):
    try:
        session = db.Session()
        dados = FuncionarioDB(None, f.nome, f.matricula, f.cpf, f.telefone, f.grupo, f.senha)
        session.add(dados)
        session.commit()
        return {"id", dados.id_funcionario}, 200
    except Exception as ex:
        session.rollback()
        return {"erro": str(ex)}, 400
    finally:
        session.close()

@router.put("/funcionario/{id}", tags=["Funcionário"])
def put_funcionario(id: int, f: Funcionario):
    try:
        session = db.Session() 
            
        dados = session.query(FuncionarioDB).filter(
            FuncionarioDB.id_funcionario == id).one()
        dados.nome = f.nome
        dados.cpf = f.cpf
        dados.telefone = f.telefone
        dados.senha = f.senha
        dados.matricula = f.matricula
        dados.grupo = f.grupo
      
        session.add(dados)
        session.commit()       
        return {"id": dados.id_funcionario}, 200   
    except Exception as ex:
        session.rollback()
        return {"erro": str(ex)}, 400
    finally:
        session.close()
        

@router.delete("/funcionario/{id}", tags=["Funcionário"])
def delete_funcionario(id: int):
    try:
        session = db.Session()      
        dados = session.query(FuncionarioDB).filter(FuncionarioDB.id_funcionario == id).one()
        session.delete(dados)
        session.commit()          
        return {"id": dados.id_funcionario}, 200      
    except Exception as ex:
        session.rollback()
        return {"erro": str(ex)}, 400
    finally: 
        session.close()