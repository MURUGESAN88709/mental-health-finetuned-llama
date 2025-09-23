from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import PeftModel
import torch
from ..core.config import settings


# tokenizer = AutoTokenizer.from_pretrained(settings.base_repo)
# base_model = AutoModelForCausalLM.from_pretrained(
#         settings.base_repo,
#         device_map="auto",
#         dtype=torch.bfloat16,
#         offload_folder="offload",
#         offload_state_dict=True,
#         trust_remote_code=True

#     ).to(settings.device)


# model = PeftModel.from_pretrained(base_model, settings.lora_repo).to(settings.device)

model = None
tokenizer = None
def generate_text(prompt: str, max_new_tokens: int = 150, temperature: float = 0.7, top_p: float = 0.9) -> str:
    return "Nothing"
    # try:
    #     inputs = tokenizer(prompt, return_tensors="pt").to(settings.device)
    #     with torch.no_grad():
    #         outputs = model.generate(
    #             **inputs,
    #             max_new_tokens=max_new_tokens,
    #             temperature=temperature,
    #             top_p=top_p,
    #             do_sample=True,
    #             pad_token_id=tokenizer.eos_token_id,
    #             eos_token_id=tokenizer.eos_token_id
    #         )
    #     return tokenizer.decode(outputs[0], skip_special_tokens=True)
    # except Exception as e:
    #     return "Could not generate now. Please try after sometime."




