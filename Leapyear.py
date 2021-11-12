'''
@Author: Md Azeem pasha
@Date: 2021-11-09
@Title : to check whether the year is leap year or not'''


def checkYear(year):
    return (((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0));

year = int(input("Enter a Year:"))
if (checkYear(year)):
    print("Leap Year")
else:
    print("Not a Leap Year")