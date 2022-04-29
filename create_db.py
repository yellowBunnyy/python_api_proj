from src import create_app, models, db
db.create_all(app=create_app())