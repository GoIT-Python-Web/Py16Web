from bson import ObjectId
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://userweb16:****@krabaton.5mlpr.gcp.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi("1"))
# Send a ping to confirm a successful connection
db = client.web16

try:
    db.cats.insert_many(
        [
            {
                "name": "Boris",
                "age": 12,
                "features": ["ходить в лоток", "не дає себе гладити", "сірий"],
            },
            {
                "name": "Murzik",
                "age": 1,
                "features": ["ходить в лоток", "дає себе гладити", "чорний"],
            },
        ]
    )
except Exception as e:
    print(e)
