import os
from flask import Flask
from dotenv import load_dotenv
from flask_login import LoginManager
from .database import db
from .models import *
from .auth import auth

load_dotenv()

app = Flask(__name__)

db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db_host = os.getenv('DB_HOST', '127.0.0.1')
db_port = os.getenv('DB_PORT', '3306')
db_name = os.getenv('DB_NAME')

login_manager = LoginManager()
login_manager.init_app(app)

app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
db.init_app(app)

# For file uploads, path needs to be changed to work on your local machine
app.config['UPLOAD_FOLDER'] = 'C:/Users/maxec/Documents/Get Into Tech/RetroFlix/application/static/careers_uploads'
app.config['MAX_CONTENT_LENGTH'] = 1 * 1024 * 1024  # 1MB max-limit.


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

app.register_blueprint(auth)



from . import routes
