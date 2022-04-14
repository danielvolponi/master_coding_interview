#!usr/bin/env python3
""" What is the Big O of the below function? 
(Hint, you may want to go line by line
"""
def fun_challenge(array): 
    a = 10 # O(1)
    a = 50 + 3 # O(1)

    for i in range(len(array)): # O(n)
        # anotherFunction() # O(n)
        stranger = True # O(n)
        a += 1 # O(n)
    
    return a # O(1)

lista = [1, 2, 3, 4, 5]
print(fun_challenge(lista))

"""
Result
3*O(1) + O(n) + O(n) + O(n) + O(n)
Big O: (3 + 4n) 
"""
