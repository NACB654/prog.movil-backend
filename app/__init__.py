from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')
    
    db.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():
        from app.models import Usuario
        from app.routes import UserRoute
        app.register_blueprint(UserRoute.bp)

    return app