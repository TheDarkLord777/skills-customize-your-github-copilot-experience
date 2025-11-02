from typing import List, Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


class Item(BaseModel):
    id: int
    name: str
    description: Optional[str] = None


app = FastAPI(title="Starter FastAPI: Items API")

# In-memory "database"
_items: List[Item] = []


@app.get("/", tags=["root"])
def read_root():
    return {"message": "Welcome to the FastAPI starter app"}


@app.get("/items/", response_model=List[Item])
def list_items():
    return _items


@app.post("/items/", response_model=Item, status_code=201)
def create_item(item: Item):
    # naive uniqueness check for example purposes
    if any(x.id == item.id for x in _items):
        raise HTTPException(status_code=400, detail="Item with this id already exists")
    _items.append(item)
    return item


@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    for it in _items:
        if it.id == item_id:
            return it
    raise HTTPException(status_code=404, detail="Item not found")


@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, updated: Item):
    for i, it in enumerate(_items):
        if it.id == item_id:
            _items[i] = updated
            return updated
    raise HTTPException(status_code=404, detail="Item not found")


@app.delete("/items/{item_id}", status_code=204)
def delete_item(item_id: int):
    for i, it in enumerate(_items):
        if it.id == item_id:
            _items.pop(i)
            return
    raise HTTPException(status_code=404, detail="Item not found")
