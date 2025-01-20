import base64
from io import BytesIO
from PIL import Image
import numpy as np
import face_recognition
import cv2

def decodificar_imagem_base64(imagem_base64):
    imagem_bytes = base64.b64decode(imagem_base64)
    imagem_pil = Image.open(BytesIO(imagem_bytes))
    imagem_np = np.array(imagem_pil)
    return imagem_np

def codificar_imagem_base64(imagem_np):
    imagem_pil = Image.fromarray(imagem_np)
    buffered = BytesIO()
    imagem_pil.save(buffered, format="JPEG")
    imagem_base64 = base64.b64encode(buffered.getvalue()).decode('utf-8')
    return imagem_base64
