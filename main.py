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

systemPrompt = "List apenas os nome dos produtos, e ofereça uma pequena descrição."
llm = genai.GenerativeModel(
    model_name=MODEL_CHOICE, 
    system_instruction=systemPrompt,
    generation_config=configure_model
    )

questions = "Liste tres produtos de moda sustentável para ir ao shopping."
response = llm.generate_content(questions)

print(f"A resposta gerada para pergunta é:\n{response.text}")