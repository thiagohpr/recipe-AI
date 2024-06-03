from typing import List
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import tensorflow as tf
from io import BytesIO
from PIL import Image as PILImage
from pydantic import BaseModel
import google.generativeai as genai
import os
# from tensorflow.keras.layers import Input
# from tensorflow.keras.models import Model
# from tensorflow.keras.layers.experimental import TFSavedModelLayer


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # This is for development only, specify domains for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model = tf.keras.models.load_model('model/',  compile=False)

# tfsmlayer = tf.keras.layers.TFSMLayer(model_path='model/', call_endpoint='serving_default')

# model_layer = TFSavedModelLayer('model/', call_endpoint='serving_default')

# If you need to incorporate this layer into a larger model:
# inputs = Input(shape=(input_shape,), dtype=tf.float32)
# outputs = model_layer(inputs)
# model = Model(inputs=inputs, outputs=outputs)

labels = {0: 'abacaxi',
 1: 'abobrinha',
 2: 'alface',
 3: 'alho',
 4: 'arroz',
 5: 'aveia',
 6: 'bacon',
 7: 'banana',
 8: 'batata',
 9: 'biscoito_oreo',
 10: 'brocolis',
 11: 'chocolate',
 12: 'couve_flor',
 13: 'filet_mignon',
 14: 'ketchup',
 15: 'laranja',
 16: 'leite',
 17: 'limao',
 18: 'linguica',
 19: 'maca',
 20: 'macarrao',
 21: 'manteiga',
 22: 'mortadela',
 23: 'mostarda',
 24: 'ovo',
 25: 'pao',
 26: 'pera',
 27: 'queijo_mussarela',
 28: 'salmao',
 29: 'sobrecoxa_frango',
 30: 'sucrilhos',
 31: 'tomate'}

@app.post("/upload")
async def upload_image(files: List[UploadFile] = File(...)):
    predictions = []
    for file in files:
        image_bytes = await file.read()
        image = PILImage.open(BytesIO(image_bytes))
        image = image.resize((230, 307))  # Adjust size to match your model's expected input
        image_array = tf.keras.preprocessing.image.img_to_array(image)
        image_array = tf.expand_dims(image_array, 0)

        prediction = model.predict(image_array)
        predicted_class = tf.argmax(prediction[0]).numpy()

        predictions.append(labels[predicted_class])

    print(predictions)

    return send_genai_request(predictions)



def send_genai_request(predictions):
    with open('google_api_key', 'r') as file:
        GOOGLE_API_KEY = file.read()

    genai.configure(api_key=GOOGLE_API_KEY)

    model = genai.GenerativeModel('gemini-pro')

    req = ','.join(predictions)

    response = model.generate_content("Write a recipe using the following ingredients {}.".format(req))

    return response.text