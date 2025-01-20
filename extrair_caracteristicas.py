import face_recognition
import cv2
import numpy as np
from decodificar_imagem import codificar_imagem_base64
from scipy.spatial import distance as dist

def extrair_caracteristicas(imagem_np):
    try:
        caracteristicas = {
            'encoding': None,
            'olhos_posicao': None,
            'boca_posicao': None,
            'nariz_posicao': None,
            'largura_rosto': None,
            'altura_rosto': None,
            'distancia_olho_olho': None,
            'distancia_olho_boca': None,
            'distancia_nariz_boca': None,
            'idade_estimada': None,
            'genero_estimado': None,
            'imagem_base64': codificar_imagem_base64(imagem_np)
        }

        locais_dos_rostos = face_recognition.face_locations(imagem_np)
        if not locais_dos_rostos:
            raise ValueError("Nenhum rosto detectado na imagem.")

        encodings = face_recognition.face_encodings(imagem_np, locais_dos_rostos)
        if not encodings:
            raise ValueError("Não foi possível extrair encodings faciais.")

        caracteristicas['encoding'] = encodings[0].tolist()

        face_landmarks_list = face_recognition.face_landmarks(imagem_np)
        if not face_landmarks_list:
            raise ValueError("Não foi possível detectar landmarks faciais.")

        top, right, bottom, left = locais_dos_rostos[0]

        largura_rosto = right - left
        altura_rosto = bottom - top
        caracteristicas['largura_rosto'] = largura_rosto
        caracteristicas['altura_rosto'] = altura_rosto

        face_landmarks = face_landmarks_list[0]
        olhos_posicao = face_landmarks.get('left_eye', []) + face_landmarks.get('right_eye', [])
        boca_posicao = face_landmarks.get('top_lip', []) + face_landmarks.get('bottom_lip', [])
        nariz_posicao = face_landmarks.get('nose_bridge', []) + face_landmarks.get('nose_tip', [])

        if olhos_posicao and boca_posicao and nariz_posicao:
            caracteristicas['olhos_posicao'] = olhos_posicao
            caracteristicas['boca_posicao'] = boca_posicao
            caracteristicas['nariz_posicao'] = nariz_posicao

            # Calcular distâncias críticas
            olho_esquerdo = np.mean(face_landmarks['left_eye'], axis=0)
            olho_direito = np.mean(face_landmarks['right_eye'], axis=0)
            boca_centro = np.mean(boca_posicao, axis=0)
            nariz_centro = np.mean(nariz_posicao, axis=0)

            distancia_olho_olho = dist.euclidean(olho_esquerdo, olho_direito)
            distancia_olho_boca = dist.euclidean(olho_esquerdo, boca_centro)
            distancia_nariz_boca = dist.euclidean(nariz_centro, boca_centro)

            caracteristicas['distancia_olho_olho'] = distancia_olho_olho
            caracteristicas['distancia_olho_boca'] = distancia_olho_boca
            caracteristicas['distancia_nariz_boca'] = distancia_nariz_boca
        else:
            raise ValueError("Não foi possível calcular posições faciais essenciais.")

        caracteristicas['idade_estimada'] = 'Indefinida'
        try:
            if altura_rosto < 120:
                caracteristicas['idade_estimada'] = '<20 anos'
            elif altura_rosto < 180:
                caracteristicas['idade_estimada'] = '20-40 anos'
            else:
                caracteristicas['idade_estimada'] = '>40 anos'
        except Exception as e:
            caracteristicas['idade_estimada'] = f"Erro: {str(e)}"

        caracteristicas['genero_estimado'] = 'Indefinido'
        try:
            proporcao_rosto = largura_rosto / altura_rosto if altura_rosto > 0 else 0
            if proporcao_rosto > 1.1:
                caracteristicas['genero_estimado'] = 'Masculino'
            elif proporcao_rosto > 0.9:
                caracteristicas['genero_estimado'] = 'Feminino'
            else:
                caracteristicas['genero_estimado'] = 'Indefinido'
        except Exception as e:
            caracteristicas['genero_estimado'] = f"Erro: {str(e)}"


    except Exception as e:
        # Log ou tratamento de erros detalhado
        caracteristicas['erro'] = str(e)

    return caracteristicas
