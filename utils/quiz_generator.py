"""
Quiz generation utilities using LLM
"""
import os
from huggingface_hub import InferenceClient
from config.settings import MODEL_CONFIG

def generate_quiz(prompt):
    """
    Generate quiz using LLM
    
    Args:
        prompt (str): The prompt template for quiz generation
        
    Returns:
        str: Generated quiz content
    """
    client = InferenceClient(
        provider=MODEL_CONFIG["provider"],
        api_key=os.getenv("HF_TOKEN")
    )
    
    messages = [{"role": "user", "content": prompt}]
    
    completion = client.chat.completions.create(
        model=MODEL_CONFIG["model"],
        messages=messages,
        temperature=MODEL_CONFIG["temperature"],
        max_tokens=MODEL_CONFIG["max_tokens"]
    )
    
    return completion.choices[0].message["content"]