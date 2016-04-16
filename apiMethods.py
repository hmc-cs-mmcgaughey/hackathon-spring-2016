import requests, json

def getWaterQuantity(foodName, quantity, unit):
    """inputs: foodName (string) - name of food
               quantity integer number of foodName items
               unit - unit specifier (eg. grams)
       output:
               float number of gallons of water in food.
    """

    url = "http://splooshed2.herokuapp.com/food?inputFood=" + foodName + "&inputAmount=" + quantity + "&inputUnit=" + unit
    
    responseQuantity = requests.get(url)

    responseFromQuery = responseQuantity.json()

    waterQuantityInGallons = responseFromQuery['gallons']

    return float(waterQuantityInGallons)

getWaterQuantity('wheat', '2', 'g')