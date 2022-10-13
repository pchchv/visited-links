from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Visited links server. Version 0.0.1"}