import os
import yaml
import torch
from pydantic_settings import BaseSettings

# Get base directory and config path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_PATH = os.path.join(BASE_DIR, "config.yaml")

# Load YAML safely outside the class
with open(CONFIG_PATH) as f:
    CONFIG = yaml.safe_load(f)

class Settings(BaseSettings):
    base_repo: str = CONFIG["base_repo"]
    lora_repo: str = CONFIG["lora_repo"]
    device: str = "cuda" if torch.cuda.is_available() else "cpu"

settings = Settings()
