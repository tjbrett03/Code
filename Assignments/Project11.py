# Thomas Brett Labouchere 
# CYB 267 Dr. Petzold
from tkinter import E 
myList = [0]
def addList(upperLimit = float(input("enter upper limit: ")), lowerLimit = float(input("enter lower limit: "))):
    i = 0
    number = (upperLimit - lowerLimit)/4 
    tempnum = number
    while i < 4:
        myList.append(number)
        number += tempnum
        print(myList)
        i += 1       
equation = lambda x : -0.5*(float(x)**3) + float(x)**2 + 2**float(x) + 1
length = len(myList)
x = 0
addList()
print(equation(myList[1:3]))