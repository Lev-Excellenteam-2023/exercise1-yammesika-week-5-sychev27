def get_recipe_price(prices, optionals=[], **ingredients):
    # Check if input is correct
    if isinstance(type(prices), dict):
        print("Incorrect input")
        return

    # Remove the optional ingredients from prices
    list_of_prices = prices
    for op_ingredient in optionals:
        del list_of_prices[op_ingredient]

    # Calculate the price of recipe
    price = 0
    if list_of_prices:
        for ingredient, amount in ingredients.items():
            price += (amount / 100) * list_of_prices[ingredient]

    print(price)


get_recipe_price({'chocolate': 18, 'milk': 8}, optionals=['milk'], chocolate=300)
get_recipe_price({})
get_recipe_price({'chocolate': 18, 'milk': 8}, optionals=['milk', 'chocolate'], chocolate=300)