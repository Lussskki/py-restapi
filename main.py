import uvicorn
from fastapi import FastAPI
from methods import route
from database import connection_db

app = FastAPI()
app.include_router(route)

if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", reload=True)
