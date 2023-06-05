#!/usr/bin/python3

"""
0-prime_game

Module to determine the winner of the prime game based on the given number of rounds and array of n.
"""

def isWinner(x, nums):
    """
    Determine the winner of each game based on the given number of rounds and array of n.

    Args:
        x (int): Number of rounds.
        nums (list): Array of n.

    Returns:
        str: Name of the player who won the most rounds. If the winner cannot be determined, returns None.
    """

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def get_next_prime(n):
        while True:
            n += 1
            if is_prime(n):
                return n

    def get_winner(n):
        if n == 1:
            return 2

        player = 1
        primes = [2]
        next_prime = 3

        while next_prime <= n:
            primes.append(next_prime)
            next_prime = get_next_prime(next_prime)

        while n > 1:
            found = False
            for prime in primes:
                if n % prime == 0:
                    n //= prime
                    found = True
                    break
            if not found:
                break
            player = 1 if player == 2 else 2

        return player

    winner_count = {1: 0, 2: 0}

    for n in nums:
        winner = get_winner(n)
        if winner is not None:
            winner_count[winner] += 1

    if winner_count[1] > winner_count[2]:
        return "Maria"
    elif winner_count[2] > winner_count[1]:
        return "Ben"
    else:
        return None

# Handle input and call the function
x = int(input("Enter the number of rounds: "))
nums = []
for i in range(x):
    num = int(input(f"Enter the value of n for round {i+1}: "))
    nums.append(num)

winner = isWinner(x, nums)
if winner is not None:
    print(f"The winner of the most rounds is: {winner}")
else:
    print("The winner cannot be determined.")
