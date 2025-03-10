from dotenv import load_dotenv
import os

load_dotenv()

# Login credentials
BUNDELING_USERNAME = os.getenv('BUNDELING_USERNAME')
BUNDELING_PASSWORD = os.getenv('BUNDELING_PASSWORD')
BUNDELING_GROUP = os.getenv('BUNDELING_GROUP')

# URLs
BASE_URL = "https://web.bundeling.com"
LOGIN_URL = f"{BASE_URL}/login"
USERS_URL = f"{BASE_URL}/bundel/landgoedgolfbanen/user"

