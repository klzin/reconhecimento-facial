import sqlite3

def criar_tabela(db_path):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS pessoas
                 (cpf TEXT, nome TEXT, nascimento TEXT, rg TEXT, mae TEXT, encoding TEXT, 
                 olhos_posicao TEXT, boca_posicao TEXT, nariz_posicao TEXT,
                 largura_rosto INTEGER, altura_rosto INTEGER,
                 distancia_olho_olho REAL, distancia_olho_boca REAL, distancia_nariz_boca REAL,
                 idade_estimada INTEGER, genero_estimado TEXT, imagem_base64 TEXT)''')  # Garantindo que temos 17 colunas
    conn.commit()
    conn.close()

def inserir_pessoa(db_path, pessoa):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    try:
        c.execute('INSERT INTO pessoas VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', pessoa)
    except sqlite3.OperationalError as e:
        print(f"Erro ao inserir pessoa: {e}")
        print(f"Valores fornecidos: {pessoa}")
    conn.commit()
    conn.close()
