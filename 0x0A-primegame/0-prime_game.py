#!/usr/bin/python3

def isWinner(x, nums):
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
            return None

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


if __name__ == '__main__':
    rounds = 3
    numbers = [4, 5, 1]
    print("Winner: {}".format(isWinner(rounds, numbers)))
