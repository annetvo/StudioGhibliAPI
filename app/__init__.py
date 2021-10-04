from flask import Flask
from config import Config
from flask_cors import CORS

from .movies.routes import movies
from .authentication.routes import auth
from .api.routes import api

from .models import db, login
from flask_migrate import Migrate


app = Flask(__name__)
cors=CORS(app, origins=['*'])

app.register_blueprint(movies)
app.register_blueprint(auth)
app.register_blueprint(api)

app.config.from_object(Config)

db.init_app(app)

migrate = Migrate(app, db)

login.init_app(app)
login.login_view = 'auth.signin'
login.login_message = 'Please log in to see this page.'
login.login_message_category = 'alert-info'


from . import routes
from . import models

