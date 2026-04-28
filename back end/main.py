from database.connection import engine
from models.base import Base

# Importar todos os models
from models.usuario import Usuario

def main():
    try:
        Base.metadata.create_all(bind=engine)
        print("Banco conectado e tabelas verificadas com sucesso!")
    except Exception as e:
        print(f"Erro ao inicializar o sistema: {e}")


if __name__ == "__main__":
    main()