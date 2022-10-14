import os
import datetime
from typing import List
from fastapi import FastAPI
from dotenv import load_dotenv
from pydantic import BaseModel
from pymongo import MongoClient


app = FastAPI()
load_dotenv('.env')
client = MongoClient(os.getenv('MONGO'))
db = client['links-database']
links = db.links

class Item(BaseModel):
    links: List[str]


@app.get('/')
async def root():
    return {'message': 'Visited links server. Version 0.0.1'}

@app.post('/visited_links')
async def create_item(item: Item):
    linksList = {"links" : item.links,
        "date": datetime.datetime.utcnow()}
    links.insert_one(linksList).inserted_id
    return {"status": "ok"}
