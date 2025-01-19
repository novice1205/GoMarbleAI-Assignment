from fastapi import FastAPI
from app.api import router

app = FastAPI()
app.include_router(router)

@app.get("/")
def read_root():
    return {"message": "GoMarble AI Engineer Assignment API is running!"}