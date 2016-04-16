Notes:

Website text
    exclude www. from api calls!
    GET splooshed2.herokuapp.com/list_foods
    returns a list of all food names understood by Splooshed.
    GET splooshed2.herokuapp.com/food?inputFood=[food]&inputAmount=[amount]&inputUnit=[unit]
    returns water-impact information for a single food of the given amount.
    POST splooshed2.herokuapp.com/recipe
    returns water-impact information for a recipe (passed in as newline-separated text).


From: http://water.usgs.gov/edu/activity-percapita.php

    Showers: 2-5 gallons per minute --> 35 gallons for a 10-min shower
    Toilet flushes: 1.6 gallons per flush
    Load of laundry: 30 gallons per load
    Load of dishes: 10 gallons (on average)

    www.conserveh20.org

    Tap: 1.5 gallons per minute (on average)
