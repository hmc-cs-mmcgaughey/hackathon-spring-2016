from flask import Flask
app = Flask(__name__)

import json
import apiMethods
from flask import render_template, request

@app.route("/")
def webDoc():
    return render_template("webDoc.html")


# @app.route("/foodComparison")
# def foodComparison():
#     return render_template("getInfoPage.html")

@app.route("/getFoodInfo")
def getFoodInfo():
    food = request.args.get("food")
    quantity = request.args.get("quantity")
    unit = request.args.get("unit")
    return render_template("getInfoPage.html")


if __name__ == "__main__":
    app.run()
