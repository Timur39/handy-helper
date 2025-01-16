from dotenv import load_dotenv
import os

load_dotenv()


list_of_admins = os.getenv("LIST_OF_ADMINS").split(', ')
github_api_token = os.getenv("GITHUB_API_TOKEN")