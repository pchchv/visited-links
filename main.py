from typing import List
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    links: List[str]


@app.get("/")
async def root():
    return {"message": "Visited links server. Version 0.0.1"}

@app.post("/visited_links")
async def create_item(item: Item):
    # TODO: Add timestamps
    # TODO: Implement data loading into the database
    return {"status": "ok"}