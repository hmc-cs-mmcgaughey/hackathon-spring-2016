from flask import Flask
from flast.ext.script import Manager, Command
app = Flask(__name__)

import json
import apiMethods
from flask import render_template, request

@app.route("/")
def webDoc():

    return render_template("webDoc.html")


@app.route("/foodComparison")
def foodComparison():

    return render_template("getInfoPage.html")

@app.route("/getFoodInfo")
def getFoodInfo():
    food = request.args.get("food")
    return


if __name__ == "__main__":
    app.run()
