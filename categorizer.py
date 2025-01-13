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

def categorizer_product(product_name, list_possible_categories):	
    systemPrompt = f"""
                Você é um categorizador de produtos.
                Você deve assumir as categorias presentes na lista abaixo.
                # Lista de Categorias Válidas
                {list_possible_categories.split(",")}
                # Formato da Saída
                Produto: Nome do Produto
                Categoria: apresente a categoria do produto
                # Exemplo de Saída
                Produto: Escova elétrica com recarga solar
                Categoria: Eletrônicos Verdes
            """
    
    llm = genai.GenerativeModel(
        model_name=MODEL_CHOICE, 
        system_instruction=systemPrompt,
        generation_config=configure_model
        )
    return llm.generate_content(product_name).text


def main(): 
    list_possible_categories = "Eletrônicos Verdes,Moda Sustentável,Produtos de Limpeza Ecológicos,Alimentos Orgânicos, Produto de Higiene Pessoal Sustentável"
    product = input("Digite o nome do produto que deseja categorizar: ")
    while product != "":
        print(f"A resposta gerada para pergunta é:\n{categorizer_product(product, list_possible_categories)}")
        product = input("Digite o nome do produto que deseja categorizar: ") 
        
if __name__ == "__main__":
    main()
