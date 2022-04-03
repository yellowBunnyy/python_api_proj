from telnetlib import DM
from dotenv import dotenv_values, load_dotenv
secrets = dotenv_values()
ADMIN = secrets["ADMIN"]
DB = secrets["SECRET"]

