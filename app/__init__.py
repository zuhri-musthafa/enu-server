from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
from flask_cors import CORS
import os

load_dotenv()

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate.init_app(app, db)

    from app.data_penerima import routes as dp_routes
    app.register_blueprint(dp_routes.data_penerima_bp)

    from app.upload_file import routes as uf_routes
    app.register_blueprint(uf_routes.upload_file_bp)

    from app.cluster import routes as cl_routes
    app.register_blueprint(cl_routes.cluster_bp)

    return app
