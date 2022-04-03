from flask import Flask
from config import DB, ADMIN

my_app = Flask(__name__)
print(DB, ADMIN)


@my_app.route('/')
def hello():
    return 'Hello, World!'

if __name__ == "__main__":
    my_app.run()