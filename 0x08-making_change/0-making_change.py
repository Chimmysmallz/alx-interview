#!/usr/bin/python3

def makeChange(coins, total):
    if total < 0:
        return 0

    # Create a list to store the minimum number of coins needed for each value
    min_coins = [float('inf')] * (total + 1)
    min_coins[0] = 0

    # Iterate through each coin value
    for coin in coins:
        # Calculate the minimum number of coins needed for each value up to the total
        for value in range(coin, total + 1):
            min_coins[value] = min(min_coins[value], min_coins[value - coin] + 1)

    if min_coins[total] == float('inf'):
        return -1

    return min_coins[total]


if __name__ == '__main__':
    print(makeChange([1, 2, 25], 37))
    print(makeChange([1256, 54, 48, 16, 102], 1453))
