# greet/src/main.py 파일

from fastapi import FastAPI

app = FastAPI()

@app.get("/greet")
def get_fortune():
    return {
        "service": "greet", 
        "message": "하이용방가방가용"
    }