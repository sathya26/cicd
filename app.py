from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()


Instrumentator().instrument(app).expose(app)

@app.get("/")
def read_root():
    return {"message": "CI/CD Working!"}

@app.get("/health")
def health():
    return {"status": "ok"}