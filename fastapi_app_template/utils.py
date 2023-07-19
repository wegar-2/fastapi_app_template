import numpy as np
from fastapi_app_template.point2d import Point2D
import pandas as pd
from loguru import logger


def get_rns(n):
    logger.info(f"Generating {n} random numbers")
    return np.random.randn(n)


def calc_fun(point: Point2D):
    """Calculate value of a function f(x, y) = x**2 + y**2"""
    logger.info(f"Calculating function f(x, y) = x**2 + y**2 value for point: {point}")
    return point.x**2 + point.y**2


def add_col(df: pd.DataFrame, colname: str):
    logger.info("Adding column of random numbers to received dataframe")
    df[colname] = np.random.randn(df.shape[0])
    return df
