from fastapi import FastAPI

app = FastAPI(docs_url="/docs")

@app.get('/')
def index():
    return {"message": "Success"}