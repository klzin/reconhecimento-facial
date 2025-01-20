import sqlite3
import face_recognition
import logging

# Configuração do logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s | %(levelname)s | %(message)s')

def comparar_rostos(encoding_referencia, db_path, limite_resultados=10, pagina=0, tolerancia=0.8):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()

    offset = pagina * limite_resultados

    query = '''
        SELECT cpf, nome, genero_estimado, encoding FROM pessoas 
        LIMIT ? OFFSET ?
    '''
    params = [limite_resultados, offset]

    logging.info(f"Executando query: {query}")
    logging.info(f"Com parâmetros: {params}")

    c.execute(query, params)
    todas_as_pessoas = c.fetchall()

    logging.info(f"Total de registros recuperados: {len(todas_as_pessoas)}")

    resultados = []
    for cpf, nome, genero_estimado, encoding_str in todas_as_pessoas:
        encoding = eval(encoding_str)
        if encoding:
            resultado = face_recognition.compare_faces([encoding], encoding_referencia, tolerance=tolerancia)
            distancia = face_recognition.face_distance([encoding], encoding_referencia)
            if resultado[0]:
                resultados.append((cpf, nome, genero_estimado, distancia[0]))
                #logging.info(f"Correspondência encontrada: CPF={cpf}, Nome={nome}, Gênero={genero_estimado}, Distância={distancia[0]}")

    conn.close()
    resultados_ordenados = sorted(resultados, key=lambda x: x[3])
    return resultados_ordenados

# Obter a codificação de referência
imagem_referencia = face_recognition.load_image_file('foto.jpg')
locais_dos_rostos_referencia = face_recognition.face_locations(imagem_referencia)
encodings_referencia = face_recognition.face_encodings(imagem_referencia, locais_dos_rostos_referencia)

if encodings_referencia:
    encoding_referencia = encodings_referencia[0]
    #logging.info(f"Codificação de referência obtida com sucesso.")
    
    db_path = 'caracteristicas.db'
    pagina = 0
    limite_resultados = 10
    tolerancia = 0.8
    resultados = comparar_rostos(encoding_referencia, db_path, limite_resultados, pagina, tolerancia)
    
    if resultados:
        print("Correspondências encontradas:")
        for resultado in resultados:
            print(f'CPF: {resultado[0]}, Nome: {resultado[1]}, Gênero: {resultado[2]}, Distância: {resultado[3]:.4f}')
    else:
        print("Nenhuma correspondência encontrada.")
else:
    print("Nenhum rosto foi encontrado na imagem de referência.")
