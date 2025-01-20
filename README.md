# Sistema de Extração de Características Faciais

Este projeto utiliza bibliotecas avançadas de visão computacional para extrair características faciais de imagens. Ele processa informações como posições de olhos, boca, nariz, proporções faciais, e realiza estimativas básicas de idade e gênero.

## 🚀 Funcionalidades

- **Detecção de rostos:** Identifica a localização do rosto em imagens.
- **Extração de características faciais:** Inclui olhos, boca, nariz e medidas específicas.
- **Estimativa de idade e gênero:** Baseada em proporções faciais, com suporte para modelos preditivos.
- **Codificação de imagem:** Converte imagens em base64 para facilitar o armazenamento e transporte.

## 🛠️ Tecnologias Utilizadas

- **Python**: Linguagem de programação principal.
- **OpenCV**: Para processamento de imagens.
- **face_recognition**: Para detecção e análise de rostos.
- **NumPy**: Manipulação de dados numéricos.
- **decodificar_imagem**: Módulo customizado para manipulação de imagens em base64.

## 📦 Instalação

Certifique-se de ter o Python 3.7 ou superior instalado em seu sistema.

1. Clone o repositório:
    ```bash
    git clone https://github.com/kevin/sistema-extracao-facial.git
    ```
2. Navegue até o diretório do projeto:
    ```bash
    cd sistema-extracao-facial
    ```
3. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

## 🖥️ Uso

1. Prepare uma imagem no formato `.jpg`, `.png`, ou similar.
2. Use o módulo principal para processar a imagem:
    ```python
    from extrair_caracteristicas import extrair_caracteristicas
    import cv2

    imagem = cv2.imread("caminho/para/imagem.jpg")
    caracteristicas = extrair_caracteristicas(imagem)
    print(caracteristicas)
    ```
3. Resultados incluem informações como largura do rosto, distância olho a olho, entre outros.

## 📋 Detalhes do Projeto

- **Criador**: Kevin
- **Versão**: 1.02
- **Licença**: MIT

## ⚙️ Contribuição

Contribuições são bem-vindas! Para contribuir:
1. Faça um fork do repositório.
2. Crie uma nova branch:
    ```bash
    git checkout -b minha-feature
    ```
3. Envie suas alterações:
    ```bash
    git push origin minha-feature
    ```
4. Abra um Pull Request.

## 🛡️ Licença

Este projeto é licenciado sob a licença MIT. Consulte o arquivo `LICENSE` para mais detalhes.

