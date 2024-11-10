import os

# Base directory for the application
BASE_DIR = "/opt/llama_api"

# Model settings
MODEL_DIR = "/opt/llama_models"
MODEL_FILENAME = "MN-Dark-Horror-The-Cliffhanger-18.5B-D_AU-IQ4_XS.gguf"
MODEL_PATH = os.path.join(MODEL_DIR, MODEL_FILENAME)
MODEL_REPO_ID = "DavidAU/MN-Dark-Horror-The-Cliffhanger-18.5B-GGUF"

# API settings
API_HOST = "0.0.0.0"
API_PORT = 5000

# Model parameters
MODEL_PARAMS = {
    "n_ctx": 512,
    "n_batch": 512,
    "chat_format": "llama-2"
}

# Default generation parameters
DEFAULT_TEMPERATURE = 0.8
DEFAULT_MAX_TOKENS = 256
