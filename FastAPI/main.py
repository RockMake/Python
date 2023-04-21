from fastapi import FastAPI

Prueba = FastAPI()


@Prueba.get("/")
async def root():
    return {"message": "Hello World"}
