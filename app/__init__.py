from flask import Flask
import sass

app = Flask(__name__)

sass.compile(dirname=('./app/static/scss', './app/static/css'))

from app import routes