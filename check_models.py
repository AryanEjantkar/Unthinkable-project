import google.generativeai as genai
from dotenv import load_dotenv, find_dotenv
import os

# Load the API key from your .env file
load_dotenv(find_dotenv())
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

print("\n🔍 Listing all Gemini models available for your API key...\n")

for m in genai.list_models():
    print(m.name)
