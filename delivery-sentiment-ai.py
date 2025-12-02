import os
from dotenv import load_dotenv
from openai import OpenAI

# carrega as variáveis do arquivo .env
# procura o arquivo .env mesmo se ele estiver na pasta de cima
load_dotenv(override=True) 

# pega a chave da memória
minha_chave = os.getenv("OPENAI_API_KEY")

# inicializa o cliente com a chave
client = OpenAI(api_key=minha_chave)


def analyze_review(review_text):
    """
    Usa GenAI para extrair sentimento e tags de um review de delivery.
    """
    prompt = f"""
    Analise o seguinte review de um pedido de delivery:
    "{review_text}"
    
    Retorne APENAS um JSON com o seguinte formato:
    {{
        "sentiment": "Positive" | "Negative" | "Neutral",
        "key_issues": [lista de problemas citados, se houver],
        "suggested_reply_tone": "Apologetic" | "Grateful" | "Excited"
    }}
    """
    
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )
    
    return response.choices[0].message.content

# teste
reviews = [
    "O sushi estava delicioso, mas chegou todo revirado na caixa. O entregador parecia com pressa.",
    "Melhor hambúrguer da vida! E chegou quentinho. Amei o recadinho na embalagem."
]

print("--- Análise de Feedback Delivery---")
for rev in reviews:
    print(f"\nReview: {rev}")
    analysis = analyze_review(rev)
    print(f"AI Analysis: {analysis}")