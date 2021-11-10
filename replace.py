'''
@Author: Md Azeem pasha
@Date: 2021-11-07
@Title :Replace String Template '''

str1 = str(input("enter the username:\n"))
txt= "Hello Username,How are you?"
replaced= txt.replace("Username",str1,1)
print(replaced)