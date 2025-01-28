from dotenv import load_dotenv
import os

load_dotenv()


github_api_token = os.getenv("GITHUB_API_TOKEN")

todoist_api_token = os.getenv("TODOIST_API_TOKEN")

client_id = os.getenv("STEPIK_CLIENT_ID")
client_secret = os.getenv("STEPIK_CLIENT_SECRET")
user_id = os.getenv("STEPIK_ID")

list_of_admins = os.getenv("LIST_OF_ADMINS").split(', ')
api_hash = os.getenv("API_HASH")
api_id = os.getenv("API_ID")

modrinth_api_token = os.getenv("MODRINTH_API_TOKEN")
modrinth_user = os.getenv("MODRINTH_USER")

CHANNELS = os.getenv("CHANNELS").split(',')

youtube_api_key = os.getenv("YOUTUBE_API_KEY")
