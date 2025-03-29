import os
from dotenv import load_dotenv

load_dotenv()

API_BOT_KEY: str = os.environ["API_BOT_KEY"]
ADMINS: list[int] = eval(os.environ["ADMINS"])
OPENAI_API_KEY: str = os.environ['OPENAI_API_KEY']  # you need to get your API key on the platform OpenAI
