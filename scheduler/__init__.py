from flask import Flask
from flask_apscheduler import APScheduler
from scheduler.config import Config

app = Flask(__name__)
app.config.from_object(Config())

scheduler = APScheduler()
scheduler.init_app(app)
