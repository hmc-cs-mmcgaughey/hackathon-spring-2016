from flask import Flask
app = Flask(__name__)

import json
import apiMethods
from flask import render_template, request

@app.route("/")
def webDoc():
    render_template("webDoc.html")
    compare = request.args.get("compare")
    info = request.args.get("info")
    if compare:
        return render_template("foodComparison.html")
    elif info:
        return render_template("getInfoPage.html")
    else:
        return render_template("webDoc.html")


@app.route("/foodComparison")
def foodComparison():
    food = request.args.get("food")
    quantity = request.args.get("quantity")
    unit = request.args.get("unit")
    return render_template("foodComparison.html")

@app.route("/getFoodInfo")
def getFoodInfo():
    food = request.args.get("food")
    quantity = request.args.get("quantity")
    unit = request.args.get("unit")
    return render_template("getInfoPage.html")


if __name__ == "__main__":
    app.run()
