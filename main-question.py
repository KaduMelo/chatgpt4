import os
import openai
openai.api_key = os.environ["OPENAI_API_KEY"]

resultado = openai.ChatCompletion.create(
    model = "gpt-3.5-turbo",
    messages = [{"role": "user", "content": "What is difference between chatgpt 3 to chatgpt 4?"}]
)

print(resultado)