from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'a8c33b31dd69aa375dd0219362687bf9'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db' 
app.app_context().push()
db = SQLAlchemy(app)

from flaskblog import routes
