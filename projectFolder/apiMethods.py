import requests, json, csv
api_key = "8nmhccHjthYxNPcUkdoiVYUfeud2hbYCsrbrjllf"

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
        return float(waterQuantityInGallons)

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

    dictionaryToReturn = {'Showers':35.0, 'Toilet':1.6, 'Laundry':30.0, 'Dishes':10.0, 'Tap':1.5}
    num = dictionaryToReturn[other]
    print num
    return waterInGallons/num

def read_csv_file( csv_file_name ):
    """
        returns a Python list of all of the data
        doesn't include the header row
        doesn't convert from strings
          == this is a _starting_ point for further data pre-processing
    """
    # is the file here?
    try:

        csvfile = open( csv_file_name, newline='' )
        csvrows = csv.reader( csvfile )              # creates a csvrows object
    except FileNotFoundError as e:
        print("File not found: ", e)


    List_of_rows = []                  # into a Python list, not yet a numpy array

    for row in csvrows:                # into our own Python data structure
        # print("row is", row)            # debugging only!

        # convert row to strings
        row = list([ str(x) for x in row])
        List_of_rows.append( row )        # add the current row _as an element_

    return List_of_rows
def showInOtherQuantity(waterInGallons, other):

    dictionaryToReturn = {'Showers':3.5, 'Toilet':1.6, 'Laundry':waterInGallons/30.0, 'Dishes':waterInGallons/10.0}

    num = dictionaryToReturn[other]
    return num

def isSimilar(new_content, original_content):
    if abs((new_content/100.0)-(original_content/100.0))<0.0001:
        return True
    else:
        return False

def compare_foods_with_similar(foodName, nutrient):

    list_of_rows = read_csv_file("ABBREV.csv")

    #find row number of nutrient
    counter = 0
    for title in list_of_rows[0]:
        if nutrient in title:
            break
        counter += 1

    original_nutrient_content = float(getNutrientContentOfFood(foodName,nutrient))
    similar_foods = []
    for i in range(1,len(list_of_rows)):
        name = list_of_rows[i][1]
        protein_content = list_of_rows[i][counter]
        if isSimilar(float(protein_content),original_nutrient_content):
            similar_foods += [name]

    try:
        return similar_foods[0:3]
    except:
        return similar_foods[0]
