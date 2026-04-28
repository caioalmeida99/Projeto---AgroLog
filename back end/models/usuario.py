# Importa os componentes necessários do SQLAlchemy
from sqlalchemy import Column, Integer, String

# Importa a classe Base, que todas as tabelas herdarão
from models.base import Base


# Classe que representa a tabela usuario
class Usuario(Base):
    
    # Nome da tabela no PostgreSQL
    __tablename__ = "usuario"

    # Chave primária da tabela
    id = Column(Integer, primary_key=True, index=True)

    # Nome do usuário (campo obrigatório)
    nome = Column(String(100), nullable=False)

    # E-mail único e obrigatório
    email = Column(String(150), unique=True, nullable=False)

    # Senha criptografada
    senha_hash = Column(String(255), nullable=False)

    # Telefone do usuário
    telefone = Column(String(20))