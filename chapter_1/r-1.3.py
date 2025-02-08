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
print(minmax(list))