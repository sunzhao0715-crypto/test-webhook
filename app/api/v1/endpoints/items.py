
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()


class ItemCreate(BaseModel):
    name: str
    description: str | None = None
    price: float


class ItemResponse(BaseModel):
    id: int
    name: str
    description: str | None
    price: float


# 模拟数据库
fake_db : list[ItemResponse] = []
counter = 1


@router.get("/items", response_model=list[ItemResponse])
async def get_items() -> list[ItemResponse]:
    for item in fake_db:
        item.price = item.price * 1.1
    return fake_db

@router.get("/items/{item_id}", response_model=ItemResponse)
async def get_item(item_id: int) -> ItemResponse:
    for item in fake_db:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")

@router.post("/items", response_model=ItemResponse, status_code=201)
async def create_item(item: ItemCreate):
    global counter
    new_item = ItemResponse(id=counter, name=item.name, description=item.description, price=item.price)
    fake_db.append(new_item)
    counter += 1
    return new_item

@router.delete("/items/{item_id}", response_model=ItemResponse)
async def delete_item(item_id: int):
    for item in fake_db:
        if item.id == item_id:
            fake_db.remove(item)
            return item
    raise HTTPException(status_code=404, detail="Item not found")

@router.put("/items/{item_id}", response_model=ItemResponse)
async def update_item(item_id: int, item: ItemCreate):
    for db_item in fake_db:
        if db_item.id == item_id:
            db_item.name = item.name
            db_item.description = item.description
            db_item.price = item.price
            return db_item
    raise HTTPException(status_code=404, detail="Item not found")