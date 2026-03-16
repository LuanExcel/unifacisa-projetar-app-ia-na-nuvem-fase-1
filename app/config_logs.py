import sys
from loguru import logger

# 1. Limpa as configurações padrão para evitar logs duplicados
logger.remove()

# 2. Configura o log no Terminal (Console) com suporte a cores e acentos
logger.add(
    sys.stderr, 
    format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>",
    colorize=True,
    enqueue=True
)

# 3. Configura o log em Arquivo com UTF-8 explícito
logger.add(
    "logs/app.log", 
    rotation="10 MB",       # Cria um novo arquivo a cada 10MB
    retention="10 days",    # Mantém logs por 10 dias
    encoding="utf-8",       # <--- ISSO resolve o problema dos acentos no arquivo
    compression="zip",      # Compacta logs antigos
    level="INFO"
)