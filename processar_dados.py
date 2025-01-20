import pandas as pd
from decodificar_imagem import decodificar_imagem_base64
from extrair_caracteristicas import extrair_caracteristicas
from database import criar_tabela, inserir_pessoa
import logging

# Configurar o logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s | %(levelname)s | %(message)s')

def processar_e_salvar_dados(csv_path, db_path):
    logging.info(f"ℹ️ Lendo o arquivo CSV: {csv_path}")
    df = pd.read_csv(csv_path, sep='|')
    logging.info(f"✅ Arquivo CSV lido com sucesso! Total de registros: {len(df)}")
    
    logging.info(f"ℹ️ Criando a tabela e índices no banco de dados: {db_path}")
    criar_tabela(db_path)
    #criar_indices(db_path)
    logging.info("✅ Tabela e índices criados com sucesso!")
    
    logging.info("ℹ️ Iniciando o processamento dos registros...")
    for index, row in df.iterrows():
        try:
            imagem_decodificada = decodificar_imagem_base64(row['foto'])
            caracteristicas = extrair_caracteristicas(imagem_decodificada)
            pessoa = (row['cpf'], row['nome'], row['nascimento'], row['rg'], row['mae'], 
                      str(caracteristicas['encoding']), str(caracteristicas['olhos_posicao']), 
                      str(caracteristicas['boca_posicao']), str(caracteristicas['nariz_posicao']), 
                      caracteristicas['largura_rosto'], caracteristicas['altura_rosto'], 
                      caracteristicas['distancia_olho_olho'], caracteristicas['distancia_olho_boca'], 
                      caracteristicas['distancia_nariz_boca'], caracteristicas['idade_estimada'], 
                      caracteristicas['genero_estimado'], caracteristicas['imagem_base64'])
            if len(pessoa) != 17:
                logging.warning(f"⚠️ Número incorreto de colunas para o registro {index}: {len(pessoa)} valores fornecidos, 17 esperados")
            inserir_pessoa(db_path, pessoa)
        except Exception as e:
            logging.warning(f"⚠️ Erro ao processar o registro {index}: {e}")

# Caminhos dos arquivos
csv_path = 'dados_1.csv'
db_path = 'caracteristicas.db'

# Processar e salvar dados
processar_e_salvar_dados(csv_path, db_path)
