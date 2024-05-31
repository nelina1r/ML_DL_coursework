import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
from GPUtil import showUtilization as gpu_usage
from numba import cuda



def free_gpu_cache():
    print("Initial GPU Usage")
    gpu_usage()

    torch.cuda.empty_cache()

    cuda.select_device(0)
    cuda.close()
    cuda.select_device(0)

    print("GPU Usage after emptying the cache")
    gpu_usage()


device = "cuda" if torch.cuda.is_available() else "cpu"
if device == "cuda":
    free_gpu_cache()

model_name = "gpt2"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)


def generate_response(theme: str) -> str:
    formatted_input = "Please give a haiku on theme " + theme
    input_ids = tokenizer.encode(formatted_input, return_tensors=None)

    with torch.no_grad():
        output = model.generate(input_ids, max_length=50)

    response = tokenizer.decode(output[0], skip_special_tokens=True)
    return tokenizer.decode(response, skip_special_tokens=True)
