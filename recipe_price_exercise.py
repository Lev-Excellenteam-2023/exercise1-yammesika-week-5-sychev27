def get_recipe_price(prices, optionals=[], **ingredients):
    """Calculate the price of a recipe based on ingredient prices and amounts.

    Args:
        prices (dict): A dictionary containing the prices of ingredients.
        optionals (list, optional): A list of optional ingredients to exclude from the price calculation.
        **ingredients: Keyword arguments specifying the amounts of ingredients used in the recipe.

    Returns:
        float: The calculated price of the recipe.

    """
    if isinstance(type(prices), dict):
        print("Incorrect input: prices should be a dictionary")
        return

    list_of_prices = prices
    for op_ingredient in optionals:
        del list_of_prices[op_ingredient]

    price = 0
    if list_of_prices:
        for ingredient, amount in ingredients.items():
            price += (amount / 100) * list_of_prices[ingredient]

    return price


def test_of_get_recipe_price():
    print(get_recipe_price({'chocolate': 18, 'milk': 8}, optionals=['milk'], chocolate=300))
    print(get_recipe_price({}))
    print(get_recipe_price({'chocolate': 18, 'milk': 8}, optionals=['milk', 'chocolate'], chocolate=300))


if __name__ == "__main__":
    test_of_get_recipe_price()