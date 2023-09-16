from urllib.parse import quote
from dotenv import find_dotenv, load_dotenv
import os

# localiza o arquivo de .env
dotenv_file = find_dotenv()

# Carrega o arquivo .env
load_dotenv(dotenv_file)

# Configurações da APP
HOST = os.getenv("HOST")
PORT = os.getenv("PORT")
RELOAD = os.getenv("RELOAD")

# Configurações de Segurança da API
X_TOKEN = os.getenv("X_TOKEN")
X_KEY = os.getenv("X_KEY")

# Configurações banco de dados
DB_SGDB = os.getenv("DB_SGDB")
DB_NAME = os.getenv("DB_NAME")
STR_DATABASE = f"sqlite:///{DB_NAME}.db"
