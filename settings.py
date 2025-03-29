import os
from dotenv import load_dotenv

load_dotenv()

API_BOT_KEY: str = os.environ["API_BOT_KEY"]
ADMINS: list[int] = eval(os.environ["ADMINS"])
