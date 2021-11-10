'''
@Author: Md Azeem pasha
@Date: 2021-11-09
@Title : Power of 2 '''

'''
@Desc : This program takes a command-line argument N and prints a table of the
powers of 2 that are less than or equal to 2^N  '''

try:
    pow = int(input("Enter the power N"))
    if pow  > 31:
        raise ValueError("entered the number greater than 31")
    num = 1
    for i in range(pow):
        num =num * 2
        print (num)
except Exception as e : # e is variable here
     print("cause of interuption  is :",e)


