import requests, json
api_key = "U6qwIj4pbaXQRdwUejhQGJdR4jh4HjBQqYMaIZac"

def getWaterQuantity(foodName, quantity, unit):
    """inputs: foodName (string) - name of food
               quantity integer number of foodName items
               unit - unit specifier (eg. grams)
       output:
               float number of gallons of water in food.
    """

    try:
        url = "http://splooshed2.herokuapp.com/food?inputFood=" + foodName + "&inputAmount=" + str(quantity) + "&inputUnit=" + unit
        responseFromQuery = requests.get(url).json()
        waterQuantityInGallons = responseFromQuery['gallons']
        return double(waterQuantityInGallons)

    except:
        return 0



def waterQuantityDifference(foodName1, foodName2, quantity1, quantity2, unit1, unit2):
    """
    computes difference for water quantities in foodname1 and 2.
    """
    waterQuantity1 = getWaterQuantity(foodName1, quantity1, unit1)
    waterQuantity2 = getWaterQuantity(foodName2, quantity2, unit2)

    return waterQuantity1-waterQuantity2

def compareWaterAndNutrition(food, nutrient):

    water = getWaterQuantity(food, 1, 'g')
    nutrients = getNutritionalContentByType(food,nutrient)

    nutrients = nutrients[0] + ' ' + nutrients[1] #combine the tuple
    water = str(water) + " gallons"

    return (nutrients, water)


def getNDBNO(foodName):

    url = "http://api.nal.usda.gov/ndb/search/?format=json&q=" + foodName + "&sort=n&max=25&offset=0&api_key=" + api_key
    responseFromQuery = requests.get(url).json()

    bestFoodResponse = responseFromQuery['list']['item'][0]

    for foodresponse in responseFromQuery['list']['item']:

        if len(bestFoodResponse['name']) > len(foodresponse['name']):
            bestFoodResponse = foodresponse




    return bestFoodResponse['ndbno']

def getNutrientID(nutrient):


    url = "http://api.nal.usda.gov/ndb/list?format=json&lt=n&max=1000&sort=n&start=0&end=1000&api_key=" + api_key
    responseFromQuery = requests.get(url).json()

    aMatch = responseFromQuery['list']['item'][0]['id']
    flag = True;

    for nutrientResponse in responseFromQuery['list']['item']:

        if nutrient == nutrientResponse['name']:
            return nutrientResponse['id']
        elif nutrient in nutrientResponse['name'] and flag:
            aMatch = nutrientResponse['id']
            flag = False

    if (flag==False):
        return aMatch

    return False


def getNutrientContentOfFood(foodName, nutrient):

    food_id = getNDBNO(foodName)
    #print("ID is", food_id)
    nutrient_id = getNutrientID(nutrient)
    #print("nutrient id is", nutrient_id)

    url = "http://api.nal.usda.gov/ndb/nutrients/?format=json"
    url += "&api_key="
    url += api_key
    url += "&ndbno="
    url += food_id
    url += "&nutrients="
    url += nutrient_id

    try:
        responseFromQuery = requests.get(url).json()
        nutrient_Value = responseFromQuery['report']['foods'][0]['nutrients'][0]['value']
        nutrient_Unit = responseFromQuery['report']['foods'][0]['nutrients'][0]['unit']

    except:
        print("couldnt find")
        return (0,0)
    
    return nutrient_Value

def showInOtherQuantity(waterInGallons, other):
    
    dictionaryToReturn = {'Showers':3.5, 'Toilet':1.6, 'Laundry':30.0, 'Dishes':10.0}
    
    num = dictionaryToReturn[other]
    return waterInGallons/num

6
