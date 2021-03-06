import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
API_TOKEN = os.environ.get("API_TOKEN")

DEFAULT_REPLY = "こんにちは！目標支援BOTです。"

PLUGINS = ['plugins']
