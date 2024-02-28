# database.py
from pymongo import MongoClient
import logging

async def connection_db():
    try:
        mongo_uri = ""
        if not mongo_uri:
            raise ValueError("Mongo DB environment variable not found")

        client = MongoClient(mongo_uri)
        db = client
        if db is not None:
            logging.info("Mongo database is connected")
            return db
        else:
            logging.error("Mongo database is not connected")
            return None
    except Exception as error:
        logging.error("Error connecting to database %s", error)
        return None
