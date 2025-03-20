import streamlit as st
import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_TOKEN = os.getenv("HF_API_TOKEN")
API_URL = "https://api-inference.huggingface.co/models/openai-community/gpt2"
headers = {"Authorization": f"Bearer {API_TOKEN}"}

def hello_world_hf():
    prompt = "Hello! Welcome to the interactive page. How are you doing?"
    payload = {
        "inputs": prompt,
        "parameters": {
            "max_new_tokens": 1,   # Must be at least 1
            "temperature": 0.1     # Low temperature for minimal variation
        },
        "options": {"wait_for_model": True}
    }
    response = requests.post(API_URL, headers=headers, json=payload)
    result = response.json()
    
    if "error" in result:
        return f"Error: {result['error']}"
    
    if isinstance(result, list) and result:
        generated_text = result[0].get("generated_text", "").strip()
        # If the returned text starts with the prompt,
        # assume any extra token is unwanted and just return the prompt.
        if generated_text.startswith(prompt):
            return prompt
        else:
            return generated_text
    return "No response generated."

def main():
    st.title("Greetings with Hugging Face")
    if st.button("Generate Message"):
        with st.spinner("Generating message..."):
            message = hello_world_hf()
        st.success("Generated Message:")
        st.write(message)


if __name__ == "__main__":
    main()
