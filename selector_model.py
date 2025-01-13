import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

kEY_API_GOOGLE = os.getenv("API_KEY_GOOGLE")
genai.configure(api_key=kEY_API_GOOGLE)
MODEL_CHOICE = "gemini-1.5-flash"
configure_model = {
    "temperature": 1.0,
    "top_p": 1.0,
    "top_k": 2,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain"
}

def load(file_name):
    try:
        with open(file_name, "r", encoding='utf-8') as file:
            data = file.read()
            return data
    except IOError as e:
        print(f"Erro ao abrir o arquivo: {e}")
        return None

systemPrompt = """
Identifique o perfil de compra para cada cliente a seguir.

O formato de saída deve ser:

cliente - descreva o perfil do cliente em 3 palavras
"""

promptUser = load("data\perfis_de_compra_100.csv")

model_flash = genai.GenerativeModel(
    model_name=MODEL_CHOICE, 
    system_instruction=systemPrompt,
    generation_config=configure_model
    )

amount_of_tokens = model_flash.count_tokens(promptUser)

tokens_limit = 1000

if amount_of_tokens.total_tokens >= tokens_limit:
    MODEL_CHOICE = "gemini-1.5-pro"

print(f"O modelo escolhido foi: {MODEL_CHOICE}")

llm = genai.GenerativeModel(
    model_name=MODEL_CHOICE, 
    system_instruction=systemPrompt,
    generation_config=configure_model
)

response = llm.generate_content(promptUser).text

print("A resposta gerada é: \n", response)