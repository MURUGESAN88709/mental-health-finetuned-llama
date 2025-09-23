from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import PeftModel
import torch

lora_repo = "ArjunRavi/mental-health-finetune"
base_repo = "NousResearch/Llama-2-7b-chat-hf"


try:
    tokenizer = AutoTokenizer.from_pretrained(base_repo)
    base_model = AutoModelForCausalLM.from_pretrained(
        base_repo,
        device_map="auto",
        dtype=torch.bfloat16
    )

    model = PeftModel.from_pretrained(base_model, lora_repo)

except Exception as e:
    print(f"Exception occured: {e}")