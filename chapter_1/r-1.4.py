"""Write a short Python function that takes a positive integer n and returns
the sum of the squares of all the positive integers smaller than n"""

def sum_sqares(n):
    total = 0
    for num in range(1, n):
        total += num ** 2
    return total

print(sum_sqares(9))

    
    
"""
get number

find all positive numbers lower than n

square each number

add the squares

return

"""    