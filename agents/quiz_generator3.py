import os
from dotenv import load_dotenv
load_dotenv()
HF_TOKEN = os.getenv("HF_TOKEN")
os.environ["HF_TOKEN"] = HF_TOKEN



from huggingface_hub import InferenceClient

client = InferenceClient(
    provider="featherless-ai",
    api_key=os.environ["HF_TOKEN"]
)
# Prompts

# messages = [{"role": "user", "content": "[translate:やさしい日本語のクイズを１つ作ってください。こたえもかいてください。]"}]
messages = [
    {
        "role": "user",
        "content": "[translate:JLPT N5のやさしい単語だけでクイズを作ってください。質問も答えも日本語で]"
    }
]


completion = client.chat.completions.create(
    model="elyza/Llama-3-ELYZA-JP-8B",
    messages=messages
)

print(completion.choices[0].message["content"])
