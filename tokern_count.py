import google.generativeai as genai
MODEL_FLASH = "gemini-1.5-flash"
MODEL_PRO = "gemini-1.5-pro"

input_cost_flash = 0.075
output_cost_flash = 0.30

input_cost_pro = 3.50
output_cost_pro = 10.50

model_flash = genai.get_model(f"models/{MODEL_FLASH}")
limit_model_flash = {
    "tokens_input": model_flash.input_token_limit,
    "tokens_output": model_flash.output_token_limit,
}

model_pro = genai.get_model(f"models/{MODEL_PRO}")
limit_model_pro = {
    "tokens_input": model_pro.input_token_limit,
    "tokens_output": model_pro.output_token_limit,
}

print(f"Os limites do modelo flash: {limit_model_flash}")
print(f"Os limites do modelo pro: {limit_model_pro}")


llm_flash =  genai.GenerativeModel(f"models/{MODEL_FLASH}")
llm_pro =  genai.GenerativeModel(f"models/{MODEL_PRO}")

num_tokens = llm_flash.count_tokens("O que é uma calça de shopping?")

print("A quantidade de tokens é: ", num_tokens)

question = llm_flash.generate_content("O que é uma calça de shopping?")
tokens_promt= question.usage_metadata.prompt_token_count
tokens_response = question.usage_metadata.candidates_token_count

total_cost_flash = (input_cost_flash * tokens_promt) / 1000000 + (output_cost_flash * tokens_response) /1000000
total_cost_pro = (input_cost_pro * tokens_promt) / 1000000 + (output_cost_pro * tokens_response) /1000000

print(f"O custo total do modelo flash é: U$ {total_cost_flash:.10f}")
print(f"O custo total do modelo pro é: U$ {total_cost_pro:.10f}")


