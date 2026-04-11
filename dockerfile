# 1. Imagem base
FROM python:3.12-slim

# 2. Define o diretório de trabalho (onde tudo vai acontecer no Linux)
WORKDIR /app

# 3. Copia o arquivo de dependências (se você tiver um)
# Se não tiver um requirements.txt, veja o passo abaixo
COPY requirements.txt .

# 4. Instala as bibliotecas necessárias
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copia todo o conteúdo da sua pasta local para dentro do container
# Isso inclui a pasta /app (com routes, schemas, etc) e o db.json
COPY . .

# 6. Expõe a porta que o FastAPI usa (padrão 8000)
EXPOSE 8000

# 7. Comando para rodar a API usando o Uvicorn
# Ajuste 'main:app' para o nome do seu arquivo principal e nome da variável FastAPI
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
