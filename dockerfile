# 1. Imagem base
FROM python:3.12-slim

# 1. Diretório base neutro no Linux, como /code
WORKDIR /code

# 2. Bixando libs
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 3. Copia TODO o seu projeto para dentro de /code
COPY . .

# 4. Define o PYTHONPATH para o Python enxergar a pasta 'code' corretamente
ENV PYTHONPATH=/code

EXPOSE 8000

# 5. Comando aponta corretamente para a pasta app que foi copiada
CMD uvicorn app.main:app --host 0.0.0.0 --port $PORT
