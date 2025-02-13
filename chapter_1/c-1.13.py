"""Write a pseudo-code description of a function that reverses a list of n
integers, so that the numbers are listed in the opposite order than they
were before, and compare this method to an equivalent Python function
for doing the same thing"""

#Psuedo-code

# reverse_list(L):
#     n = len(L)
#     for i in range(n//2):
#         L[i], L[n-i-1] = L[n-i-1], L[i]
#     return L

# Python function
def reverse_list(L):
    n = len(L)
    for i in range(n//2):
        L[i], L[n-i-1] = L[n-i-1], L[i]
    return L

# Testing the function
print(reverse_list([1, 2, 3, 4, 5]))