from fastapi import FastAPI
from pydantic import BaseModel
import google.generativeai as genai
import os

class Image(BaseModel):
    image: str

app = FastAPI()

@app.post("/recipe/")
async def create_item(image: Image):

    return 'Recebido'


genai.configure(api_key=os.environ["GEMINI_API_KEY"])
model = genai.GenerativeModel('gemini-pro')

lista_alimentos= ['carne', 'leite', 'ovo', 'arroz']
req = ','.join(lista_alimentos)

response = model.generate_content("Write a recipe using the following ingredients {}.".format(req))


