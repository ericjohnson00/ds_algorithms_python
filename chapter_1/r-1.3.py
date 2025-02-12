<<<<<<< HEAD
"""Write a short Python function, minmax(data), that takes a sequence of
one or more numbers, and returns the smallest and largest numbers, in the
form of a tuple of length two. Do not use the built-in functions min or
max in implementing your solution."""


def minmax(data):
    high = data[0]
    low = data[1]
    for num in data[1:]:
        if num < low:
            low = num
        if num > high:
            high = num
    return (low, high)

list = [6,9,2,7]
=======
"""Write a short Python function, minmax(data), that takes a sequence of
one or more numbers, and returns the smallest and largest numbers, in the
form of a tuple of length two. Do not use the built-in functions min or
max in implementing your solution."""


def minmax(data):
    high = data[0]
    low = data[1]
    for num in data[1:]:
        if num < low:
            low = num
        if num > high:
            high = num
    return (low, high)

list = [6,9,2,7]
>>>>>>> cf6c21828d7637aa1b60fa3bd26747b4f98e4ce0
print(minmax(list))