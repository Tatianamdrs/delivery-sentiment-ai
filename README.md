# Delivery Sentiment AI

> Uma ferramenta de análise de sentimento e classificação automática de reviews de delivery utilizando GenAI.

## O Problema
Em operações de delivery em larga escala, ler e classificar feedbacks manualmente é inviável. Este projeto utiliza **Large Language Models (LLMs)** para estruturar dados não estruturados (texto livre), permitindo insights rápidos sobre a operação.

## Tecnologias Utilizadas
* **Python 3.12**
* **OpenAI API (GPT-3.5 Turbo)**git push
* **Prompt Engineering** (Role-playing & JSON Formatting)
* **Git/GitHub** para versionamento

## Funcionalidades
* **Análise de Sentimento:** Classifica o review como *Positive*, *Negative* ou *Neutral*.
* **Extração de Tags:** Identifica problemas chave (ex: "Embalagem danificada", "Atraso").
* **Sugestão de Tom:** Recomenda o tom ideal para a resposta do suporte (ex: "Apologetic", "Grateful").
* **Resiliência:** Sistema de fallback para simulação caso a API esteja indisponível.
