
import os
from crewai import LLM
from dotenv import load_dotenv

load_dotenv()

try:
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("ERROR: GEMINI_API_KEY not found")
        exit(1)
        
    print(f"Initializing LLM with key length: {len(api_key)}")
    
    llm = LLM(
        model="gemini/gemini-1.5-flash",
        google_api_key=api_key,
        temperature=0.7
    )
    print("LLM initialized object created.")
    
    import google.generativeai as genai
    genai.configure(api_key=api_key)
    
    print("Listing available models...")
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            if 'gemini' in m.name:
                print(m.name)
            
    # Try to generate content
    print("Attempting to generate content...")
    response = llm.call([{"role": "user", "content": "Hello, are you working?"}])
    print(f"SUCCESS: Generation response: {response}")
    
except Exception as e:
    print(f"ERROR_DETAILS: {e}")
