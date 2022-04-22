#!usr/bin/env python3
""" What is the Big O of the below function? 
(Hint, you may want to go line by line
"""
def(input):
    a = 5 # O(1)
    b = 10 # O(1)
    c = 50 # O(1)
    for i in input: # O(n)
        x = i + 1 # O(n)
        y = i + 2 # O(n)
        z = i + 3 # O(n)

    for j in input: # O(n)
        p = j * 2 # O(n)
        q = j * 2 # O(n)

    who_am_i = "I don't know" # O(1)

"""
Result:
4*O(1) + 4*O(n) + 3*O(n)
Big O: (4 + 7n) or O(n)
"""
