import os
import openai
openai.api_key = os.environ["OPENAI_API_KEY"]

resultado = openai.Image.create(
   prompt = "A family with a couple children playing a stadium soccer and reading english books",
   n = 1,
   size = "1024x1024"
)

print(resultado)