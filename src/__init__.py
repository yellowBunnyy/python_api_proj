from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import ADMIN, SQLALCHEMY_DATABASE_URI


# init SQLAlchemy so we can use it later in our models
db = SQLAlchemy()


def create_app():
    my_app = Flask(__name__)

    my_app.config["ADMIN"] = ADMIN
    my_app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI

    db.init_app(my_app)

    # blueprint for auth routes in our app
    from .auth import auth as auth_blueprint
    my_app.register_blueprint(auth_blueprint)

    # blueprint for non-auth parts of app
    from .main import main as main_blueprint
    my_app.register_blueprint(main_blueprint)
    return my_app
