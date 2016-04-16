import requests, json

def getWaterQuantity(foodName, quantity, unit):
    """inputs: foodName (string) - name of food
               quantity integer number of foodName items
               unit - unit specifier (eg. grams)
       output:
               float number of gallons of water in food.
    """

    url = "http://splooshed2.herokuapp.com/food?inputFood=" + foodName + "&inputAmount=" + str(quantity) + "&inputUnit=" + unit
    
    responseFromQuery = requests.get(url).json()
    
    waterQuantityInGallons = responseFromQuery['gallons']

    return float(waterQuantityInGallons)

def waterQuantityDifference(foodName1, foodName2):
    """
    computes difference for water quantities in foodname1 and 2.
    """
    waterQuantity1 = getWaterQuantity(foodName1, 1, 'g')
    waterQuantity2 = getWaterQuantity(foodName2, 1, 'g')
    
    return abs(waterQuantity1-waterQuantity2)


def getNutritionalContent(foodName):
    
    url = "http://api.nal.usda.gov/ndb/nutrients/?format=json&api_key=DEMO_KEY&nutrients=205&nutrients=204&nutrients=208&nutrients=269"
    responseFromQuery = requests.get(url).json()
    
    allFoods = responseFromQuery['report']['foods']
    
    for food in allFoods:
        if foodName in food['name']:
            return food
    
    return False


def getNutritionalContentByType(food, nutrient):
    
    if (getNutritionalContent(food)==False):
        print('food doesnt have any nutritional content??')
        return False
    
    foodData = getNutritionalContent(food)
    
    for currentNutrient in foodData['nutrients']:
        if nutrient in currentNutrient['nutrient']:
            return (currentNutrient['value'],currentNutrient['unit'])
    
    print('couldnt find the nutrient in the food??')
    return False

def compareWaterAndNutrition(food, nutrient):
    
    water = getWaterQuantity(food, 1, 'g')
    nutrients = getNutritionalContentByType(food,nutrient)
    
    nutrients = nutrients[0] + ' ' + nutrients[1] #combine the tuple
    water = str(water) + " gallons"
    
    return(nutrients, water)
