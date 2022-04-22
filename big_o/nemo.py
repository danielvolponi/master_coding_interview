#!usr/bin/env python3
"""Finding Nemo

A function that looks for the string nemo of a list.
"""

import time


nemo = ['nemo']

everyone = [
    'dory', 'bruce', 'marlin', 'nemo', 'gill', 'bloat', 
    'nigel', 'squirt', 'darla', 'hank'
]

small_list = ['nemo' for i in range(10)]
medium_list = ['nemo' for i in range(100)]
large_list = ['nemo' for i in range(10000)]

def find_nemo(array):
    # t0 = time.time()
    for i in array:
        print('running')
        if i == 'nemo':
            print('Found Nemo')
            break
    # t1 = time.time()
    # print(f'Call to find Nemo took {t1 - t0}')

find_nemo(everyone)
