from fastapi import FastAPI
from fastapi_app_template.utils import get_n_rns

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/get_rns/{n}")
async def get_rns_endpoint(n: int):
    return dict(zip(range(n), get_n_rns(n)))


# running the app: use the command: uvicorn main:app --reload in the CLI
