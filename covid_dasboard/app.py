from flask import Flask, render_template
from datetime import timedelta

app = Flask(__name__)

@app.route("/")
def home():
    return "hello world"

