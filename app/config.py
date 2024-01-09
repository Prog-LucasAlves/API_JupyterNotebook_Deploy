"""Config. Connection Database"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

import os
import dotenv

# Carregando as variáveis de ambiente do arquivo .env
dotenv.load_dotenv(dotenv_path=".env.prod")

# Obtendo as variáveis de ambiente do banco de dados
db_user = os.getenv('POSTGRES_USER')
db_password = os.getenv('POSTGRES_PASSWORD')
db_name = os.getenv('POSTGRES_DB')
db_host = os.getenv('DB_HOST')
db_port = 5432

# Criando a engine com o banco de dados
DATABASE_URL = f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
engine = create_engine(DATABASE_URL)

# Criando a sessão com o banco de dados
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

# Criando a classe base
Base = declarative_base()


# Função para criar uma sessão com o banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        # Fechando a sessão com o banco de dados
        db.close()
