from flask import Flask
app = Flask(__name__)

import json
from flask import render_template, request

@app.route("/")
def index():
    return render_template("index.html")
