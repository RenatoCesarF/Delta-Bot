from dotenv import load_dotenv
from os.path import join, dirname
import os

class EnvVars():
    def __init__(self):
        self.APLICATION_ID = ''
        self.PUBLIC_KEY = ''
        self.TOKEN = ''

        dotenv_path = join(dirname(__file__), '../.env')
        load_dotenv(dotenv_path)

        self.APLICATION_ID = os.environ.get("APLICATION_ID")
        self.PUBLIC_KEY = os.environ.get("PUBLIC_KEY")
        self.TOKEN = os.environ.get("TOKEN")
      