#!usr/bin/env python3
"""Log first two Boxes

A function that prints the first two elements of an array.
O(1) -> constant time
For every input only process one element indepent of the 
amount of elements
"""

boxes = [0, 1, 2, 3, 4, 5, 6]

def log_first_two_boxes(array):
    print(array[0]) # O(1)
    print(array[1]) # O(1)

log_first_two_boxes(boxes) # O(2)
