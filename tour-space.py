# This function takes in an array of prices.

# weekly_prices = [4000, 21000, 3000, 11000, 2500, 7000, 25000, 18000, 24000, 12000, 1500, 19000]

# def tour_price(arr):
#     max_price = max(arr)
#     min_price = min(arr)
#     max_index = arr.index(max_price)
#     min_index = arr.index(min_price)
#     print("Details for the maximum difference between travel for weekly prices provided are as follows:")
#     print("The most expensive week is week {} with a travel cost of ${}.".format(max_index + 1, max_price))
#     print("The least expensive week is week {} with a travel cost of ${}.".format(min_index + 1, min_price))
#     print("The difference between the prices having had traveled during these two weeks is ${}.".format(max_price - min_price))
#     print("\n")

# tour_price(weekly_prices)


# This function takes in a dictionary of key value pairs with the keys labeled as the week number and the value set to be that weeks price.

# weekly_prices_dictionary = {"week_1": 4000, "week_2": 21000, "week_3": 3000, "week_4": 11000, "week_5": 2500, "week_6": 7000, "week_7": 25000, "week_8": 18000, "week_9": 24000, "week_10": 12000, "week_11": 1500, "week_12": 18000}

# def tour_price_dictionary(atlas):
#     value_arr = list(atlas.values())
#     prices = sorted(value_arr)
#     max_week = max(prices)
#     min_week = min(prices)
#     max_price_week = value_arr.index(max_week) + 1
#     min_price_week = value_arr.index(min_week) + 1
#     print("Details for the maximum difference between travel for weekly prices provided are as follows:")
#     print("The most expensive week is week {} with a travel cost of ${}.".format(max_price_week, max_week))
#     print("The least expensive week is week {} with a travel cost of ${}.".format(min_price_week, min_week))
#     print("The difference between the prices having had traveled during these two weeks is ${}.".format(max_week - min_week))

# tour_price_dictionary(weekly_prices_dictionary)

weekly_prices = [4000, 21000, 3000, 11000, 2500, 7000, 25000, 18000, 24000, 12000, 1500, 19000]

def tour_price(arr, go, lv):
    max_price = max(arr)
    min_price = min(arr)
    max_index = arr.index(max_price)
    min_index = arr.index(min_price)
    depart_price = arr[go - 1]
    return_price = arr[lv - 1]
    print("Details for the maximum difference between travel for weekly prices provided are as follows:")
    print("The most expensive week is week {} with a travel cost of ${}.".format(max_index + 1, max_price))
    print("The least expensive week is week {} with a travel cost of ${}.".format(min_index + 1, min_price))
    print("The difference between the prices having had traveled during these two weeks is ${}.".format(max_price - min_price))
    print("\n")
    if depart_price - return_price < 0 and go <= lv:
        difference = (depart_price - return_price) * -1
        print("The difference between your departure price and return price is ${}.".format(difference))
        print("Based on your desired departure and return dates the total cost of your trip will be ${}.".format(depart_price + return_price))
        print("\n")
    elif depart_price - return_price > 0 and go <= lv:
        print("The difference between your departure price and return price is ${}.".format(depart_price - return_price))
        print("Based on your desired departure and return dates the total cost of your trip will be ${}.".format(depart_price + return_price))
    else:
        print("You cannot travel back in time. Choose correct travel dates.")
    print("\n")
    config_weeks = arr[go:]
    # print(config_weeks)
    def subtract_price(num):
        return depart_price - num
    neg_differences = list(map(subtract_price, config_weeks))
    # print(neg_differences)
    def make_diffs_pos(num):
        if num < 0:
            return num * -1
        else:
            return num * 1
    pos_differences = list(map(make_diffs_pos, neg_differences))
    # print(pos_differences)
    max_diff = max(pos_differences)
    min_diff = min(pos_differences)
    max_diff_week = pos_differences.index(max_diff) + go + 1
    min_diff_week = pos_differences.index(min_diff) + go + 1
    # print(max_diff_week)
    # print(min_diff_week)
    print("Information regarding your return options based on your week {} departure choice:".format(go))
    print("\n")
    print("The largest difference in cost you can incur when returning is the result of coming back to earth in week {}.".format(max_diff_week))
    print("The smallest difference in cost you can incur when returning is the result of coming back to earth in week {}.".format(min_diff_week))

tour_price(weekly_prices, 2, 6)