import os

from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

# CSRF対策
app.config['DATA_DIR'] = "./manzai/data"
app.config['SECRET_KEY'] = os.urandom(32)
app.config['WTF_CSRF_ENABLED'] = os.urandom(32)
from manzai import views