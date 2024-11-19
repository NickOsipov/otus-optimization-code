"""
Script: tasks.py
Description: invoke tasks from the command line
"""

import os

from invoke import task
from invoke.context import Context
from dotenv import load_dotenv


load_dotenv()

DATA_GDRIVE_ID = os.getenv("DATA_GDRIVE_ID")

@task
def download_data(ctx: Context) -> None:
    """
    Download the data
    """
    ctx.run(f"gdown {DATA_GDRIVE_ID} -O data/reviews.csv")
