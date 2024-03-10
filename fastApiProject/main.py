from fastapi import FastAPI
from pydantic.v1 import BaseSettings


class Settings(BaseSettings):
    APP_ENV: str = 'dev'


Settings = Settings()
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
