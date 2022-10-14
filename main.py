from datetime import datetime
import os
from sqlite3 import Timestamp
import time
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
        "timestamps": time.time_ns()}
    links.insert_one(linksList).inserted_id
    return {"status": "ok"}

@app.get('/visited_domains')
async def read_item(fromTime: int, toTime: int):
    res = []
    for link in links.find():
        if fromTime < link['timestamps'] < toTime:
            for l in link['links']:
                if '?' in l:
                    l = l.split('?')[0]
                else:
                    ll = l.split('/')
                    l = ll[0] + "//" + ll[2]
                res.append(l)
    return {"domains": set(res), "status": "ok"}
