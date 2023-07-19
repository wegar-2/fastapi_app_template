from fastapi import FastAPI
from fastapi_app_template.utils import get_rns, calc_fun, add_col
from fastapi_app_template.point2d import Point2D
import pandas as pd
import numpy as np
from loguru import logger

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/get_rns/{n}")
async def get_rns_endpoint(n: int):
    return dict(zip(range(n), get_rns(n)))


@app.post("/calc_fun")
async def do_calc_fun(point: Point2D):
    # point = point.model_dump()
    logger.info(f"point: {point}")
    return {"funval": calc_fun(point)}
    # return point


# @app.post("/add_col/")
# async def add_column_to_dataframe(json_df: str, colname: str):
#     return add_col(df=pd.read_json(json_df), colname=colname).to_json()


# running the app: use the command: uvicorn main:app --reload in the CLI
