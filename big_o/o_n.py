#!usr/bin/env python3
"""Finding Nemo

A function that looks for the string nemo of a list.
O(n) -> linear time 
It takes linear time to find nemo
For every input the script have to do one operation
"""

nemo = ['nemo']

small_list = ['nemo' for i in range(10)]
medium_list = ['nemo' for i in range(100)]
large_list = ['nemo' for i in range(10000)]

def find_nemo(array):
    for i in array:
        if i == 'nemo':
            print('Found Nemo')


find_nemo(large_list)
