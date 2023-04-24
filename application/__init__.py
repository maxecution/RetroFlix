from flask import Flask
#from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
#db = SQLAlchemy(app)

from application import routes

app.secret_key = 'retroflix_is_better_than_netflix'