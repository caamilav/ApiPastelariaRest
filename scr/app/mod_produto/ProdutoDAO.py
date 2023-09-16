from fastapi  import APIRouter, Depends
from domain.entities.mod_produto.Produto import Produto
from infra.orm.mod_produto.ProdutoModel import ProdutoDB

import db
import security

router = APIRouter(dependencies=[Depends(security.verify_token), Depends(security.verify_key)])

@router.get("/produto/", tags=["Produto"])
def get_produto():
    try:
        session = db.Session()
        dados = session.query(ProdutoDB).all()
        
        if len(dados) == 0:
            return "Nenhum registro encontrado", 200
        
        return dados, 200
    except Exception as ex:
        return {"erro": str(ex)}, 400
    finally:
        session.close()

@router.get("/produto/{id}", tags=["Produto"])
def get_produto(id: int):
    try:
        session = db.Session()
        dados = session.query(ProdutoDB).filter(ProdutoDB.id_produto == id).one()
        return dados, 200
    except Exception as ex:
        return {"erro": str(ex)}, 400
    finally:
        session.close()


@router.post("/produto/", tags=["Produto"])
def post_produto(p: Produto):
    try:
        session = db.Session()
        dados = ProdutoDB(None, p.nome, p.descricao, p.foto, p.valor_unitario)
        session.add(dados)
        session.commit()
        return {"id", dados.id_produto}, 200
    except Exception as ex:
        session.rollback()
        return {"erro": str(ex)}, 400
    finally:
        session.close()

@router.put("/produto/{id}", tags=["Produto"])
def put_produto(id: int, p: Produto):
    try:
        session = db.Session() 
            
        dados = session.query(ProdutoDB).filter(
            ProdutoDB.id_produto == id).one()
        dados.nome = p.nome
        dados.descricao = p.descricao
        dados.foto = bytes(p.foto, 'utf-8')
        dados.valor_unitario = p.valor_unitario
      
        session.add(dados)
        session.commit()       
        return {"id": dados.id_produto}, 200   
    except Exception as ex:
        session.rollback()
        return {"erro": str(ex)}, 400
    finally:
        session.close()

@router.delete("/produto/{id}", tags=["Produto"])
def delete_produto(id: int):
    try:
        session = db.Session()      
        dados = session.query(ProdutoDB).filter(ProdutoDB.id_produto == id).one()
        session.delete(dados)
        session.commit()          
        return {"id": dados.id_produto}, 200      
    except Exception as ex:
        session.rollback()
        return {"erro": str(ex)}, 400
    finally: 
        session.close()