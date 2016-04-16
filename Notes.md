Notes:

Website text
    exclude www. from api calls!
    GET splooshed2.herokuapp.com/list_foods
    returns a list of all food names understood by Splooshed.
    GET splooshed2.herokuapp.com/food?inputFood=[food]&inputAmount=[amount]&inputUnit=[unit]
    returns water-impact information for a single food of the given amount.
    POST splooshed2.herokuapp.com/recipe
    returns water-impact information for a recipe (passed in as newline-separated text).
