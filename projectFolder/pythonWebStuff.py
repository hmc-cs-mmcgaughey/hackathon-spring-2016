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

@app.route("/home")
def home():
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

    waterDiff = apiMethods.waterQuantityDifference(food1, food2, quantity1, quantity2, unit1, unit2)
    firstGreaterThanSecond = (waterDiff > 0)
    waterDiff = abs(waterDiff)
    return render_template("foodComparison.html", waterDiff=waterDiff, firstGreaterThanSecond=firstGreaterThanSecond, food1=food1, food2=food2)

@app.route("/foodCompareVisual")
def foodCompareVisual():
    repToUse = request.args.get("visualChoice")
    waterDiff = request.args.get("waterDiff")
    food1 = request.args.get("food1")
    food2 = request.args.get("food2")
    waterDiff = abs(float(waterDiff))
    numReps = apiMethods.showInOtherQuantity(waterDiff,repToUse)
    return render_template("foodComparison.html", numReps = numReps, repToUse=repToUse, waterDiff=waterDiff, food1=food1, food2=food2)

@app.route("/foodSingleRepVisual")
def foodSingleRepVisual():
    repToUse = request.args.get("visualChoice")
    waterQuantity = request.args.get("waterQuantity")
    food = request.args.get("food")
    waterQuantity = abs(float(waterQuantity))
    numReps = apiMethods.showInOtherQuantity(waterQuantity, repToUse)
    return render_template("getInfoPage.html", waterQuantity = waterQuantity, numReps=numReps, repToUse = repToUse, food = food)

@app.route("/getFoodInfo")
def getFoodInfo():
    food = request.args.get("food")
    quantity = request.args.get("quantity")
    unit = request.args.get("unit")

    waterQuantity = apiMethods.getWaterQuantity(food, quantity, unit)

    return render_template("getInfoPage.html", waterQuantity=waterQuantity, food=food, quantity=quantity, unit=unit)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/sources")
def sources():
    return render_template("sources.html")

if __name__ == "__main__":
    app.run(debug = True)
