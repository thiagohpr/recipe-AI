# recipe-AI 
Felipe Drummond

Thiago Hampl

## Project Setup
- Install the backend requirements
```
pip install -r requirements.txt
```

- Unzip the model.zip file on the backend directory

- To use the Gemini google LLM, an API key is necessary. Generate one in https://ai.google.dev/gemini-api/docs/api-key?hl=pt-br and paste it on the backend/google_api_key file

## Running the project

- To run the backend, open the powershell with the projects libraries required and type:
```
uvicorn route:app
```
Wait until some tensorflow warnings appear and the message "Uvicorn running on http://127.0.0.1:8000" is on the terminal

- To run the frontend, simply execute the frontend/Release/recipe_ai_flutter.exe

- The button "Pick More Images" opens the file picker and lets the user select one or more groceries images

- After selecting the images, the button "Get Recipe" send a request to the backend and then waits for the recipe response

- The groceries predicted by the model are printed on the backend powershell window

- There are some test images on dataset/test directory to be used while testing the app

## Other Files
- The "train_model.ipynb" has the jupyter notebook used on Google Colab to train the model of the project
  
