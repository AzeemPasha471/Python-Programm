'''
@Author: Md Azeem pasha
@Date: 2021-11-10
@Title :Quadratic equation'''


'''
Desc : ( Taking  a, b and c as input values)
delta = b*b - 4*a*c
Root  of x = (-b + sqrt(delta))/(2*a)
Root  of x = (-b - sqrt(delta))/(2*a)
'''

from math import sqrt
import math

try:
    a= float(input("a : "))
    b=float(input("b : "))
    c = float(input(" c : "))

    delta = b * b - 4 * a *c
    sqrtOfDeta= math.sqrt(abs(delta))

    if delta > 0:
        print("Roots are real and unequal")
        print((-b + sqrtOfDeta) / (2 * a))
        print((-b - sqrtOfDeta) / (2 * a))

    elif delta == 0:
        print("Roots are real and equal")
        print(-b / (2 * a))

    else:
        print(" Roots are real and imaginary")
        print(- b / (2 * a), " + i", sqrtOfDeta)
        print(- b / (2 * a), " - i", sqrtOfDeta)
except:
    print("Invalid input as you enter string value")