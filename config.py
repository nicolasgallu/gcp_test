import os
from dotenv import load_dotenv

load_dotenv()

WPP_TOKEN = os.environ.get("WPP_TOKEN")
WPP_ID = os.getenv("WPP_ID")