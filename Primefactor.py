'''
@Author: Md Azeem pasha
@Date: 2021-11-09
@Title : Prime Factors of number '''

import math
factors = []
def prime_factors(n):
    #even numbers
    while (n % 2 == 0):
        factors.append(2)
        n = n / 2
    #odd numbers
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while (n % i) == 0:
            factors.append(i)
            n = n / i
    if n > 2:
        factors.append(n)
    print(factors)

n= int(input("Enter number:"))
prime_factors(n)