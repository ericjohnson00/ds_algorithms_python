"""Write a short Python function that takes a positive integer n and returns
the sum of the squares of all the odd positive integers smaller than n"""

def sum_of_squares(n):
    return sum([x**2 for x in range(1, n) if x % 2 != 0])

print(sum_of_squares(10)) # 165