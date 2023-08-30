# Making Change

This program calculates the fewest number of coins needed to meet a given total amount by using a pile of coins with different values.


## Requirements

- Python 3.4.3 or higher
- Ubuntu 14.04 LTS

## Problem Description
You are given a pile of coins with different values, and your goal is to determine the fewest number of coins needed to meet a given total amount.

The program provides the function makeChange(coins, total) which takes in two parameters:

### coins: A list of coin values in your possession.
### total: The total amount to be met using the coins.
The function returns the fewest number of coins needed to meet the total amount. The following conditions apply:

If the total is 0 or less, the function returns 0.
If the total cannot be met by any number of coins you have, the function returns -1.
The value of a coin is always an integer greater than 0.
You can assume you have an infinite number of each denomination of coin in the list.

## Example
print(makeChange([1, 2, 25], 37))  # Output: 7
print(makeChange([1256, 54, 48, 16, 102], 1453))  # Output: -1

## Usage

1. Clone the repository:

```bash
git clone https://github.com/your-username/making-change.git

cd making-change

./0-making_change.py

