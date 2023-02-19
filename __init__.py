import secrets

from flask import Flask
from flask_bootstrap import Bootstrap5
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)
bootstrap5 = Bootstrap5(app)
csrf = CSRFProtect(app)
login_manager = LoginManager(app)

from . import routes
