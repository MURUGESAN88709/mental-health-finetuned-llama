from pydantic_settings import BaseSettings
import yaml
import torch

class Settings(BaseSettings):
    with open('config.yaml') as file:
        config = yaml.load(file)
    base_repo: str = config["base_repo"]
    lora_repo: str = config["lora_repo"]
    device: str = "cuda"  if torch.cuda.is_available() else "cpu"
settings = Settings()
