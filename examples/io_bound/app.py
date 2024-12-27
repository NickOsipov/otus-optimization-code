"""
Sync fetch data from a server
"""

import os
from typing import Annotated

import pandas as pd
from fastapi import FastAPI, Path
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """
    Settings for the application
    """

    data_path: str = os.path.join("data", "reviews.csv")


settings = Settings()
df = pd.read_csv(settings.data_path)
app = FastAPI()


@app.get("/")
def get_root():
    """
    Helthcheck endpoint
    """
    return {"message": "Hello"}


@app.get("/total")
async def get_total():
    """
    Total number of texts
    """
    return {"total": df.shape[0]}


@app.get("/texts/{text_id}")
async def get_text(text_id: Annotated[int, Path(ge=0, lt=df.shape[0])]):
    """
    View text by id
    """
    return {"text": df.iloc[text_id]["review"]}
