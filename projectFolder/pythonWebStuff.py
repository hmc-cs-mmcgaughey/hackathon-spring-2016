from flask import Flask
app = Flask(__name__)

import json
from flask import render_template, request

@app.route("/")
def webDoc():
    # return "Hello!"
    return render_template("webDoc.html")

if __name__ == "__main__":
    app.run()
