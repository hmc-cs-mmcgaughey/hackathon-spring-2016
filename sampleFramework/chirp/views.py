import os

import json
from flask import render_template, request
from yelpapi import YelpAPI
from firebase import firebase

from chirp import app

yelp_api = YelpAPI(os.environ['YELP_KEY'], os.environ['YELP_SECRET'],
                   os.environ['YELP_TOKEN'], os.environ['YELP_TOKEN_SECRET'])

firebase = firebase.FirebaseApplication("https://yelphackweek.firebaseio.com", None)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/save", methods=["POST"])
def save():
	image_url = request.form.get("image_url")
	description = request.form.get("description")
	rating = request.form.get("rating")
	name = request.form.get("name")

	firebase.post("/Restaurants", {
		"image_url" : image_url,
		"description" : description,
		"name" : name,
		"rating" : rating
	})

	return "Saved!"

@app.route("/favorites")
def favorites():
	# query firebase for the current favorites
	restaurants = firebase.get("/Restaurants", None)
	businesses = []
	for key in restaurants:
		businesses.append(restaurants[key])

	return render_template("index.html", businesses=businesses)


@app.route("/search")
def search():
    try:
        yelp_rs = yelp_api.search_query(location=request.args.get("location"))
        yelp_bs = yelp_rs["businesses"]

        businesses = []
        for b in yelp_bs:
        	businesses.append({
        		"image_url" : b["image_url"][:-6] + "ls.jpg",
        		"name" : b["name"],
        		"description" : b["snippet_text"],
        		"rating" : b["rating_img_url"]
        	})

        # businesses = [{"image_url": i['image_url'][:-6] + 'ls.jpg', "busid": i["id"]}
        #           for i in yelp_rs['businesses']]

    except (YelpAPI.YelpAPIError):
        return "Oops! Error!"
    return render_template("index.html", businesses=businesses)
