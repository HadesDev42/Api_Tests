#!/usr/bin/env python3

import json
from fastapi import FastAPI


app = FastAPI()
f = open("data.json", "r")
db = json.load(f)
print(len(db["items"]))
t = ""

@app.get("/help")
async def help():
    return """Welcome to this basic API, you have 3 methods : GET, POST, DELETE.
            "GET :
            "To get all the items, you can use the following url : http://localhost:8000/items
            "To get a specific item, you can use the following url : http://localhost:8000/items/id=<item_id>

            "POST :
            "To add an item, you can use the following url : http://localhost:8000/items/add?name=<NAME>

            "DELETE :
            "To delete an item, you can use the following url : http://localhost:8000/items/delete?id=<item_id>"""

@app.get("/items")
async def read_item(id: int = 0):
    if id == 0:
        return db["items"]
    if (id > len(db["items"])):
        return "Error id not found, try to add it with items/add?... method"
    return db["items"][id-1]

@app.get("/items/add")
async def add_item(name: str):
    item = { "id": len(db["items"])+1,"title": name }
    db["items"].append(item)
    with open("data.json", "w") as f:
        json.dump(db, f)
    return item, "Added"

@app.get("/items/delete")
async def delete_item(id: int):
    if (id > len(db["items"])):
        return "Error id not found, try to add it with items/add?... method"
    t = db["items"][id-1]["title"]
    db["items"].pop(id-1)
    with open("data.json", "w") as f:
        json.dump(db, f)
    return "Deleted", t