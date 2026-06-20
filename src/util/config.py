from dotenv import load_dotenv
from os import getenv

load_dotenv()

class Config:
    CON_STRING = getenv('CON_STRING')

config = Config()