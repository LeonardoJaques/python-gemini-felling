import os
import google.generativeai as genai
from dotenv import load_dotenv
from google.api_core.exceptions import NotFound

load_dotenv()

kEY_API_GOOGLE = os.getenv("API_KEY_GOOGLE")
genai.configure(api_key=kEY_API_GOOGLE)
MODEL_CHOICE = "gemini-1.5-flashxxx"
configure_model = {
    "temperature": 1.0,
    "top_p": 1.0,
    "top_k": 2,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain"
}

def analizer_fellins(nameProduct):
    global MODEL_CHOICE

    def load(file_name):
        try:
            with open(file_name, "r", encoding='utf-8') as file:
                data = file.read()
                return data
        except IOError as e:
            print(f"Erro ao abrir o arquivo: {e}")
            return None
        

    def save(file_name, data):
        try:
            with open(file_name, "w", encoding='utf-8') as file:
                file.write(data)
                return True
        except IOError as e:
            print(f"Erro ao salvar o arquivo: {e}")
            return False
        
    systemPrompt = f"""
            Você é um analisador de sentimentos de avaliações de produtos.
            Escreva um parágrafo com até 50 palavras resumindo as avaliações e
            depois atribua qual o sentimento geral para o produto.
            Identifique também 3 pontos fortes e 3 pontos fracos identificados a partir das avaliações.

            # Formato de Saída

            Nome do Produto:
            Resumo das Avaliações:
            Sentimento Geral: [utilize aqui apenas Positivo, Negativo ou Neutro]
            Ponto fortes: lista com três bullets
            Pontos fracos: lista com três bullets
        """    

    promptUser = load(f"data/avaliacoes-{nameProduct}.txt")


    print(f"Analise de sentimentos para o produto: {nameProduct}")

    for attempt in range(2):
        try:
            llm = genai.GenerativeModel(
                model_name=MODEL_CHOICE, 
                system_instruction=systemPrompt,
                generation_config=configure_model
            )       
            response = llm.generate_content(promptUser).text
            save(f"data/result-{nameProduct}.txt", response)
            break
        except NotFound as e:
            print(f"Erro ao acessar o modelo: {e}")
            if attempt == 0:
                MODEL_CHOICE = "gemini-1.5-flash"
                print("Failed to access the model again.")
                print("Falha ao tentar acessar o modelo novamente.")


def main():
    listProducts = ["Camisetas de algodão orgânico", "Jeans feitos com materiais reciclados","Maquiagem mineral"]
    for product in listProducts:
        analizer_fellins(product)

if __name__ == "__main__":
    main()