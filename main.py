from fastapi import FastAPI
from app.routes import empresa_routes

app = FastAPI()

app.include_router(empresa_routes.router)

@app.get("/")
def home():
    return {"message": "Emissor de NFSe rodando!"}