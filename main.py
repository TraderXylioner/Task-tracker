from fastapi import FastAPI, APIRouter
from uvicorn import run

app = FastAPI()

# base router
base_router = APIRouter(prefix='/api')

# v1 router
v1_router = APIRouter(prefix='/v1')

base_router.include_router(v1_router)
app.include_router(base_router)

if __name__ == "__main__":
    run("main:app")
