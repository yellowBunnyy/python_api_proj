from dotenv import dotenv_values
secrets = dotenv_values()
ADMIN = secrets["ADMIN"]
DB = secrets["SECRET"]
