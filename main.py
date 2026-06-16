from typing import Optional
from fastapi import FastAPI
from pymongo import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://lexws33:KdkPwU2AZ4wU9jNL@cluster0.f0fjujx.mongodb.net/?appName=Cluster0"
app = FastAPI()
client = MongoClient(uri, server_api=ServerApi('1'))

@app.get("/")
async def root():
    # Send a ping to confirm a successful connection
    try:
        client.admin.command('ping')
        return {"Pinged your deployment. You successfully connected to MongoDB!"}
    except Exception as e:
        return {"Error": "Unable to connect to the database."}
    

@app.get("/users/{user_name}")
async def get_user(user_name: str):
    db = client["users"]
    collection = db["Plain Users"]
    user = collection.find_one({"name": user_name})
    if user:
        return {"user": user}
    else:
        return {"Error": "User not found."}

# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Optional[str] = None):
#     return {"item_id": item_id, "q": q}

