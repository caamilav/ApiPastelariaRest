from fastapi import FastAPI
from settings import HOST, PORT, RELOAD
from app.mod_funcionario import FuncionarioDAO
from app.mod_cliente import ClienteDAO
from app.mod_produto import ProdutoDAO

app = FastAPI()

# mapeamento das rotas/endpoints
app.include_router(FuncionarioDAO.router)
app.include_router(ClienteDAO.router)
app.include_router(ProdutoDAO.router)

import db
db.createTable()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run('apiPastelaria:app', host=HOST, port=int(PORT), reload=RELOAD)
    
    
