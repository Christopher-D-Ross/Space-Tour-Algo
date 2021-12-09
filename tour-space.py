# This function takes in an array of prices.

weekly_prices = [4000, 21000, 3000, 11000, 2500, 7000, 25000, 18000, 24000, 12000, 1500, 18000]

def tour_price(arr):
    max_price = max(arr)
    min_price = min(arr)
    max_index = arr.index(max_price)
    min_index = arr.index(min_price)
    print("Details for the maximum difference between travel for weekly prices provided are as follows:")
    print("The most expensive week is week {} with a travel cost of ${}.".format(max_index + 1, max_price))
    print("The least expensive week is week {} with a travel cost of ${}.".format(min_index + 1, min_price))
    print("The difference between the prices having had traveled during these two weeks is ${}.".format(max_price - min_price))
    print("\n")

tour_price(weekly_prices)


# This function takes in a dictionary of key value pairs with the keys labeled as the week number and the value set to be that weeks price.

weekly_prices_dictionary = {"week_1": 4000, "week_2": 21000, "week_3": 3000, "week_4": 11000, "week_5": 2500, "week_6": 7000, "week_7": 25000, "week_8": 18000, "week_9": 24000, "week_10": 12000, "week_11": 1500, "week_12": 18000}

def tour_price_dictionary(atlas):
    value_arr = list(atlas.values())
    prices = sorted(value_arr)
    max_week = max(prices)
    min_week = min(prices)
    max_price_week = value_arr.index(max_week) + 1
    min_price_week = value_arr.index(min_week) + 1
    print("Details for the maximum difference between travel for weekly prices provided are as follows:")
    print("The most expensive week is week {} with a travel cost of ${}.".format(max_price_week, max_week))
    print("The least expensive week is week {} with a travel cost of ${}.".format(min_price_week, min_week))
    print("The difference between the prices having had traveled during these two weeks is ${}.".format(max_week - min_week))

tour_price_dictionary(weekly_prices_dictionary)