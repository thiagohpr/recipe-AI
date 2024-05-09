from fastapi import FastAPI
from pydantic import BaseModel

class Image(BaseModel):
    image: str

app = FastAPI()

@app.post("/recipe/")
async def create_item(image: Image):

    return 'Recebido'