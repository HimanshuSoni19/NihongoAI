import os
from dotenv import load_dotenv
load_dotenv()
HF_TOKEN = os.getenv("HF_TOKEN")

from huggingface_hub import InferenceClient
API_TOKEN = HF_TOKEN

MODEL_ID = "elyza/ELYZA-japanese-Llama-2-7b"

client = InferenceClient(token=API_TOKEN)

prompt = "[translate:日本語学習者向けのシンプルなクイズ問題を1つ作成してください。答えも含めてください。]"

response = client.text_generation(model=MODEL_ID, prompt=prompt)

print(response.generated_text)


