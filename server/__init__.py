# server/__init__.py
from flask import Flask
from dotenv import load_dotenv
import os

from server.config import Config
from server.extensions import db, jwt, ma, migrate
from server.routes.auth_routes import auth_bp
from server.routes.order_routes import order_bp
from server.routes.product_routes import product_bp
from server.routes.unsplash_routes import unsplash_bp  # ✅ Import the Unsplash blueprint

def create_app(): 
    app = Flask(__name__) 

    # Load environment variables
    load_dotenv()

    # Config from environment
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI', 'sqlite:///db.sqlite3')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY', 'your-secret-key')

    # Initialize extensions
    db.init_app(app)
    ma.init_app(app)
    jwt.init_app(app)
    migrate.init_app(app, db)

    # Register blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(product_bp)
    app.register_blueprint(order_bp, url_prefix='/orders')
    app.register_blueprint(unsplash_bp, url_prefix='/api')  # ✅ Register Unsplash route

    @app.route('/')
    def home():
        return 'Welcome to Fashion Hub Backend API!'
  
    return app
