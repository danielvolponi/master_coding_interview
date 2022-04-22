#!usr/bin/env python3
"""Log all pairs of array

A function that prints the first two elements of an array.
O(1) -> constant time
For every input only process one element indepent of the 
amount of elements
"""

boxes = [0, 1, 2, 3, 4, 5]


def log_all_pairs(list_):
    for n1 in list_:
        for n2 in list_:
            print(f"{n1}, {n2}")
            
log_all_pairs(boxes) 
