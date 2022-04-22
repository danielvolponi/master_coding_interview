#!usr/bin/env python3
"""Space Complexity
"""

n = [1, 2, 3, 4, 5]
def boooo(n):
    for i in n:
        print('Booooooo!')

# boooo([1, 2, 3, 4, 5])

# O(n) and space complexity of O(1)
"""
Talking about space complexity we are not adding much 
more memory O(1), we dont care about input,
but how is processed
"""

def hi_n_times(n):
    hi_list = []
    for i in n:
        hi_list.append('hi')

    print(hi_list)

hi_n_times(n)

"""
O(n)
Space Complexity we are creating a new array and filled 
them with O(n). We are adding additional memory.
"""
