'''
@Author: Md Azeem pasha
@Date: 2021-11-10
@Title :Calculate the distance between 2 points'''

import math

try:
    a = input("enter first coordinate : ")
    p1 = a.split(",")

    b = input("enter second coordinate : ")
    p2 = b.split(",")

    distance = math.sqrt(((int(p1[0]) - int(p2[0])) ** 2) + ((int(p1[1]) - int(p2[1])) ** 2))
    print(distance)

except Exception as e:

    print(e)