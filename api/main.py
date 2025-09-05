from fastapi import FastAPI
from .routers import upload, analyze

app = FastAPI()

app.include_router(upload.router)
app.include_router(analyze.router)


@app.get("/")
def read_root():
    return {"Hello": "World"}
