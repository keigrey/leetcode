def max_profit(prices: list[int]) -> int:
    """
    Given an array prices where prices[i] is the price of a given stock on the ith day
    return the maximum profit you can achieve from this transaction.
    If you cannot achieve any profit, return 0.
    :param prices:
    :return: maximum profit
    """

    price_hash = {
        "cheap_price": prices[0],
        "cheap_index": 0,
        "expensive_price": prices[0],
        "expensive_index": 0
    }

    for i, price in enumerate(prices):
        if price <= price_hash["cheap_price"]:
            price_hash["cheap_price"] = price
            price_hash["cheap_index"] = i
            price_hash["expensive_price"] = price
            price_hash["expensive_index"] = i
        if price >= price_hash["expensive_price"]:
            price_hash["expensive_price"] = price
            price_hash["expensive_index"] = i

    if price_hash["expensive_index"] <= price_hash["cheap_index"]:
        return 0
    else:
        return price_hash["expensive_price"] - price_hash["cheap_price"]


def test(expected: int, actual: int):
    if expected == actual:
        print("⭕")
    else:
        print(f"❌\nexpected: {expected}\nactual:{actual}")
    
    
test(5, max_profit([7, 1, 5, 3, 6, 4]))
test(0, max_profit([7, 6, 4, 3, 1]))
