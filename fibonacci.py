#Import python built in module
from functools import lru_cache

@lru_cache()
def fibonacci(n):
    #Check that the input is a positive integer
    if type(n) != int:
        raise TypeError("n must be a positive int")
    if n < 1:
        raise ValueError("n must be a positive int")
    #Compute the Nth term
    if n == 1 or n == 2:
        return 1
    elif n > 2:
        return fibonacci(n-1) + fibonacci(n-2)

for i in range(1, 201):
    print(i, ":", fibonacci(i))
