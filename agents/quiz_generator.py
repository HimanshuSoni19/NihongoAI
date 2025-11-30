
# this code did not work as my cuda needs pytorch 2.6 and it is not good as of right now and I need to wait, I can use hugging face key instead of using using downloaded elyza llm, I read it from the access key

import torch
#print(torch.cuda.is_available())
#print(torch.cuda.current_device())
#print(torch.cuda.get_device_name(0))

#print(torch.__version__)

from transformers import AutoModelForCausalLM, AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("elyza/ELYZA-japanese-Llama-2-7b")
#model = AutoModelForCausalLM.from_pretrained("elyza/ELYZA-japanese-Llama-2-7b")
model = AutoModelForCausalLM.from_pretrained("elyza/ELYZA-japanese-Llama-2-7b-safetensors", torch_dtype=torch.float16, safe_serialization=True)

device = torch.device("cpu")
model = model.to(device)
def generate_japanese_quiz():
    prompt = "日本語学習者向けのシンプルなクイズ問題を1つ作成してください。答えも含めてください。"
    input_ids = tokenizer(prompt, return_tensors="pt").input_ids
    output = model.generate(input_ids, max_new_tokens=100)
    generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
    print(generated_text)

if __name__ == "__main__":
    generate_japanese_quiz()
