import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY not found")

genai.configure(api_key=api_key)

# 🔴 DO NOT USE: "gemini-1.5-flash" / "gemini-1.5-latest"
# ✅ USE ONE OF THE 2.x MODELS:
model = genai.GenerativeModel("gemini-2.5-flash")  # or "gemini-2.5-pro"

response = model.generate_content("Say 'Hello from Gemini 2.5!'")
print(response.text)
