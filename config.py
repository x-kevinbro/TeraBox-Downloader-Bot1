from dotenv import load_dotenv
load_dotenv()

import os

class BOT:
    TOKEN = os.environ.get("TOKEN", "8145794920:AAHMHrOyl9LuKg6jNWQzUizTBe7N6hGe2VQ")

class API:
    HASH = os.environ.get("API_HASH", "771c072b4ae280c10508d636b494b285")
    ID = int(os.environ.get("API_ID", 25013204))

class OWNER:
    ID = int(os.environ.get("OWNER", 8046796637))

class CHANNEL:
    ID = int(os.environ.get("CHANNEL_ID", -1002804547624))

class WEB:
    PORT = int(os.environ.get("PORT", 8080))

class DATABASE:
    URI = os.environ.get("DB_URI", "mongodb+srv://damiruimo:ABVvGpyR8fVe7nar@x-kevin.83vo1.mongodb.net/")
    NAME = os.environ.get("DB_NAME", "Cluster0")
