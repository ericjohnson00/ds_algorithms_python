"""Write a short Python function that takes a sequence of integer values and
determines if there is a distinct pair of numbers in the sequence whose
product is odd."""

def distinct_pair(seq):
    for i in range(len(seq)):
        for j in range(i+1, len(seq)):
            if (seq[i] * seq[j]) % 2 != 0:
                return True
    return False

# Test cases
print(distinct_pair([1, 2, 3, 4, 5]))  # True
print(distinct_pair([2, 4, 6, 8, 10]))  # False