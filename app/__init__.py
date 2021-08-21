from flask import Flask
from sassutils.wsgi import SassMiddleware
import sass

app = Flask(__name__)
app.config["SECRET_KEY"] = "key"

app.wsgi_app = SassMiddleware(app.wsgi_app, {
    'app': ('static/scss', 'static/css', '/static/css')
})

sass.compile(dirname=('./app/static/scss', './app/static/css'))

from app import routes