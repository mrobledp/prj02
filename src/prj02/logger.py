import logging
import os
from dotenv import load_dotenv

# Cargar .env
load_dotenv()

# Niveles configurables
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO").upper()
LIB_LOG_LEVEL = os.getenv("LIB_LOG_LEVEL", "WARNING").upper()

# Crear carpeta de logs si no existe
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

LOG_FILE = os.path.join(LOG_DIR, "prj02.log")

# Configuración del logger principal
logging.basicConfig(
    level=getattr(logging, LOG_LEVEL, logging.INFO),
    format="%(asctime)s [%(levelname)s] %(name)s - %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE, encoding="utf-8"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("prj02")

# 🔥 Ajustar nivel de log de librerías externas
for lib in ["boto3", "botocore", "urllib3", "s3transfer"]:
    logging.getLogger(lib).setLevel(getattr(logging, LIB_LOG_LEVEL, logging.WARNING))

# 🔥 Línea que siempre muestra el nivel de log activo
logger.info(f"INICIO DEL PROCESO CON Nivel de log activo: {LOG_LEVEL} (librerías: {LIB_LOG_LEVEL})")