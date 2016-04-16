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
    food1 = request.args.get("food1")
    quantity1 = request.args.get("quantity1")
    unit1 = request.args.get("unit1")
    food2 = request.args.get("food2")
    quantity2 = request.args.get("quantity2")
    unit2 = request.args.get("unit2")

    waterDiff = waterQuantityDifference(food1, food2, quantity1, quantity2, unit1, unit2);


    return render_template("foodComparison.html")

@app.route("/getFoodInfo")
def getFoodInfo():
    food = request.args.get("food")
    quantity = request.args.get("quantity")
    unit = request.args.get("unit")
    return render_template("getInfoPage.html")

@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run()
