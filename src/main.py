from fastapi import FastAPI
from MathHandler import MathHandler

app = FastAPI(docs_url="/docs")
mathHandler = MathHandler()

@app.get('/')
def index():
    return {"message": "Success"}

@app.get('/math/index')
def mathIndex():
    return mathHandler.index()