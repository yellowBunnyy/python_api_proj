from dotenv import dotenv_values
secrets = dotenv_values()
ADMIN = secrets["ADMIN"]
SQLALCHEMY_URI = secrets["SQLALCHEMY_URI"]
