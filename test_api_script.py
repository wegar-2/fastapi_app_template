import numpy as np
import pandas as pd
import requests
from loguru import logger
from fastapi_app_template.point2d import Point2D


if __name__ == '__main__':

    url = "http://127.0.0.1:8000"

    logger.info("testing endpoint /get_rns/{n}...")
    res = requests.get(url + "/get_rns/10")
    logger.info(f"Received response: {res.json()}")

    logger.info("testing endpoint /calc_fun...")
    res = requests.post(
        url=url + "/calc_fun/",
        json={"x": 1.0, "y": 2.0}
    )
    logger.info(f"Received response: {res.status_code}")
    logger.info(f"Received response: {res.content}")

    # df = pd.DataFrame(data={"X": np.random.randn(10), "Y": np.random.randn(10)})
    # df.to_json()
    # requests.get()