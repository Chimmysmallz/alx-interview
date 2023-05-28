#!/usr/bin/python3

def makeChange(coins, total):
    """
    Calculate the fewest number of coins needed to meet a given total amount.

    Args:
        coins (list): List of coin values.
        total (int): Target total amount.

    Returns:
        int: Fewest number of coins needed to meet the total. Returns -1 if the total cannot be met.

    """

    if total <= 0:
        return 0

    # Create a list to store the fewest number of coins needed for each total amount
    min_coins = [float('inf')] * (total + 1)
    min_coins[0] = 0

    for i in range(1, total + 1):
        for coin in coins:
            if coin <= i:
                min_coins[i] = min(min_coins[i], min_coins[i - coin] + 1)

    if min_coins[total] == float('inf'):
        return -1

    return min_coins[total]


if __name__ == "__main__":
    print(makeChange([1, 2, 25], 37))
    print(makeChange([1256, 54, 48, 16, 102], 1453))
