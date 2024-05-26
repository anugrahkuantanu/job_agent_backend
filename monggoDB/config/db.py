
from dotenv import load_dotenv
import motor.motor_asyncio

load_dotenv()


MONGODB_URL="mongodb://localhost:27017/job_agent"


client = motor.motor_asyncio.AsyncIOMotorClient(MONGODB_URL)

db = client.job_agent
# users_collection = db.get_collection("users")
users_collection = db["users"]
jobs_collection = db["jobs"]

