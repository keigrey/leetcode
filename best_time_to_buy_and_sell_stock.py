def max_profit(prices: list[int]) -> int:
    """
    Given an array prices where prices[i] is the price of a given stock on the ith day
    return the maximum profit you can achieve from this transaction.
    If you cannot achieve any profit, return 0.
    :param prices:
    :return: maximum profit
    """

    l, r = 0, 1  # left -> buy, right -> sell
    maximum_profit = 0

    while r < len(prices):
        if prices[l] < prices[r]:
            profit = prices[r] - prices[l]
            maximum_profit = max(maximum_profit, profit)
        else:
            l = r
        r += 1

    return maximum_profit



def test(expected: int, actual: int):
    if expected == actual:
        print("⭕")
    else:
        print(f"❌\nexpected: {expected}\nactual:{actual}")
    
    
test(5, max_profit([7, 1, 5, 3, 6, 4]))
test(0, max_profit([7, 6, 4, 3, 1]))
test(2, max_profit([2, 4, 1]))

