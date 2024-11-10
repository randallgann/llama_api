from llama_cpp import Llama
import os
from .config import MODEL_DIR, MODEL_PATH, MODEL_REPO_ID, MODEL_FILENAME, MODEL_PARAMS

class ModelManager:
    _instance = None

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def __init__(self):
        self.model = self._initialize_model()

    def _initialize_model(self):
        """Initialize the model if it doesn't exist in the specified directory"""
        if not os.path.exists(MODEL_DIR):
            os.makedirs(MODEL_DIR)
        
        if not os.path.exists(MODEL_PATH):
            print(f"Downloading model to {MODEL_PATH}...")
            Llama.from_pretrained(
                repo_id=MODEL_REPO_ID,
                filename=MODEL_FILENAME,
                model_path=MODEL_PATH
            )
        
        return Llama(
            model_path=MODEL_PATH,
            **MODEL_PARAMS
        )

    def generate(self, messages, temperature=None, max_tokens=None):
        """Generate response using the model"""
        from .config import DEFAULT_TEMPERATURE, DEFAULT_MAX_TOKENS
        
        return self.model.create_chat_completion(
            messages=messages,
            temperature=temperature or DEFAULT_TEMPERATURE,
            max_tokens=max_tokens or DEFAULT_MAX_TOKENS
        )
