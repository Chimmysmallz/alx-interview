#!/usr/bin/python3
def minOperations(n):
    if n % 2 == 1:
        return 0
    count = 0
    h_count = 2
    while h_count < n:
        if n % h_count == 0:
            count += 2  # copy all and paste
            h_count *= 2
        else:
            count += 1  # paste
            h_count += h_count
    if h_count == n:
        count += 2  # copy all and paste
    return count
