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
    cmd = f"gdown {DATA_GDRIVE_ID} -O data/reviews.csv"
    print(cmd)
    ctx.run(cmd)

@task
def run_app(ctx: Context) -> None:
    """
    Run the application
    """
    cmd = "uvicorn examples.io_bound.app:app --port 5002 --reload"
    print(cmd)
    ctx.run(cmd)

@task
def view_profile(ctx: Context, profile: str) -> None:
    """
    View the application profile
    """
    profile_path = os.path.join("examples", "optimization", "profiles", f"{profile}.prof")
    cmd = f"snakeviz {profile_path}"
    print(cmd)
    ctx.run(cmd)
