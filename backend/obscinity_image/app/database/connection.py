from pymongo import MongoClient
import pymongo
from ..user_auth.config import settings

# Create a MongoClient instance instead of using mongo_client.MongoClient
client = MongoClient(settings.DATABASE_URL, serverSelectionTimeoutMS=5000)

try:
    # Use the `is_master` command to check the server connection instead of `server_info`
    conn = client.admin.command("isMaster")
    print(f'Connected to MongoDB {conn.get("version")}')

except pymongo.errors.ServerSelectionTimeoutError:
    print("Unable to connect to the MongoDB server.")


# Access the database directly from the client instance
db = client.get_database(settings.MONGO_INITDB_DATABASE)

obscenity_collection = db.NSFW