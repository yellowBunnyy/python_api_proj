from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from .config import SECRET, SQLALCHEMY_DATABASE_URI


# init SQLAlchemy so we can use it later in our models
db = SQLAlchemy()


def create_app():
    my_app = Flask(__name__)

    my_app.config['SECRET_KEY'] = SECRET
    my_app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
    my_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

    db.init_app(my_app)
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(my_app)

    from .models import User
    @login_manager.user_loader
    def load_user(user_id):
        # since the user_id is just the primary key of our user table, use it in the query for the user
        return User.query.get(int(user_id))


    # blueprint for auth routes in our app
    from .auth import auth as auth_blueprint
    my_app.register_blueprint(auth_blueprint)

    # blueprint for non-auth parts of app
    from .main import main as main_blueprint
    my_app.register_blueprint(main_blueprint)
    return my_app
