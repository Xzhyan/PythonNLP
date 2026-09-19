from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path


# Caminho absoluto
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Diretorio de dados
DATA_DIR = BASE_DIR / 'data'

# Diretorio de arquvos JSON
JSON_DIR = DATA_DIR / 'json'

# Arquivo json do vocabulário
VOCAB_JSON = JSON_DIR / "vocabulary.json"

# Diretorio de npy
NPY_DIR = DATA_DIR / 'npy'

# Arquivo de embedding.npy
EMBEDDING_FILE = NPY_DIR / 'embedding.npy'


class Settings(BaseSettings):
    """Configurações do projeto"""

    APP_NAME: str = "PythonIA"

    # model_config = SettingsConfigDict(
    #     env_file=".env"
    # )


settings = Settings()
