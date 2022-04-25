from dotenv import dotenv_values
secrets = dotenv_values()
SECRET = secrets["SECRET"]
SQLALCHEMY_DATABASE_URI = secrets["SQLALCHEMY_DATABASE_URI"]
