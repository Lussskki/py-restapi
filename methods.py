# methods.py
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from database import connection_db

class Item(BaseModel):
    name: str
    last: str

route = APIRouter()

@route.post("/")
async def add_method(item: Item):
    db = await connection_db()
    try:
        if db is not None:
            result = db.insert_one(item.dict())
            inserted_id = result.inserted_id
            return {"inserted_id": str(inserted_id)}
        else:
            raise HTTPException(status_code=500, detail="Failed to connect to database")
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to add item to database")
    finally:
        if db:
            db.client.close()
