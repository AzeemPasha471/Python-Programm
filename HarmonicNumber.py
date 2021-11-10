'''
@Author: Md Azeem pasha
@Date: 2021-11-09
@Title : Harmonic number programm'''
try:
    num = int(input("Enter the Number: "))
    assert num!=0
except:
    print("Number Is Zero")
else:
    harmonic=0
    for i in range(1,num+1):
        harmonic=harmonic+1/i
        print(harmonic)