"""Give a single command that computes the sum from Exercise R-1.6, 
relying on Python’s comprehension syntax and the built-in sum function."""


print(sum([n ** 2 for n in range(1, 10) if n % 2 != 0])) # 165