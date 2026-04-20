from database.connection import engine

try:
    connection = engine.connect()
    print("Conectado com sucesso!")
    connection.close()
except Exception as e:
    print("Erro ao conectar:", e)