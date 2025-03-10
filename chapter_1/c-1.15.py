"""Write a Python function that takes a sequence of numbers and determines
if all the numbers are different from each other (that is, they are distinct)."""

def are_different(seq):
    return len(seq) == len(set(seq))

print(are_different([1, 2, 3, 4, 5])) # True