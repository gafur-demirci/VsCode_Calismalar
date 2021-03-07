#%% Ex1

num = int(input("Kaç sayı girmek istiyorsunuz ? "))
total_sum = 0

for n in range(num):
    numbers = float(input("Sayı giriniz : "))
    total_sum += numbers

avg = total_sum / num
print("Average is : ",avg)

#%% Ex2

n = int(input("Sayı giriniz : "))

sum_n = (n*(n + 1))/2
print("{0} tane pozitif tam sayının toplamı : ".format(n),sum_n)
#%% Ex3

import time

def myFunc():
    start_time = time.time()
    s = 0
    for i in range(1, n+1):
        s += i
    
    end_time = time.time()
    return s , end_time-start_time

n = 5
print(myFunc())
#%% Ex4

import getpass

print(getpass.getuser())
#%% Ex5

import os

print(os.environ["HOMEDRIVE"])
print(os.environ["PATH"])
#%% Ex6

import  sys

print("Python Version")
print(sys.version)
print(sys.version_info)
#%% Ex7

import  datetime

now = datetime.datetime.now()
print("Current date and time is : ", now.strftime("%y-%m-%d : %H:%M:%S"))
#%% Ex8

import math

radius = float(input("Please give me the radius : "))
print("Area of a circle of radius {0} : ".format(radius),(math.pi*(radius**2)))
#%% Ex9

fName = input("Write to FirstName : ")
lName = input("Write to LastName : ")
name = [fName,lName]
print(name[-1] + " " + name[0])
print(lName + " " + fName)
#%% Ex10

values = input("İnput some numbers : ")
liste = list(values.split(sep=","))
tuples = tuple(liste)

print("List : ", liste, "Tuple : " , tuples)
#%% Ex11

fileName = input("Write the file name : ")
file_ext = fileName.split(".")
print("File name : " , file_ext[0] + " , " +  "File ext : " , file_ext[1])

# repr a bak
#%% Ex12

colors = []
while True:
    color = input("Write some colors : ")
    if color == "end":
        break
    else:
        colors.append(color)

print("First color is : " , colors[0], "Last color is : " , colors[-1])
#%% Ex13

import datetime
exam_date = datetime.datetime(2012,5,12,15,45,00,00)
print("Exam date is : ",exam_date)
#%% Ex14

n = str(input("Write a number : "))
print(" n + nn + nnn is : ", int(n)+ int(n+n)+ int(n+n+n))
#%% Ex15

print(int.__doc__)
#%% Ex16

import calendar

year = int(input("Enter the year : "))
month = int(input("Enter the month : "))
print(calendar.month(year, month))
#%% Ex17

print("""
This 
        text is 

    my without
                    having escape
            in
                Python
""")
#%% Ex18

import datetime

firstDate = datetime.date(1996,2,20)
lastDate = datetime.date(2021,3,6)

print(lastDate-firstDate)
#%% Ex19

import math

radius = float(input("Please give me the radius : "))

volumeOfSphere = ((4/3) * math.pi * (radius**3))
areaOfSphere = 4 * math.pi * (radius**2)

print("Radius is {} of Sphere's Area :".format(radius), str(areaOfSphere) + "\n" +"Radius is {} of Sphere's Volume :".format(radius), str(volumeOfSphere))
#%% Ex20

def difference(number1,number2):
    if number1 <= number2:
        return number2 - number1
    else:
        return number1 - number2

print(difference(20,30))
#%% Ex21

def sumThreeNums(num1,num2,num3):
    if num1 == num2 == num3:
        return num1 * 3
    else:
        return num1 + num2 + num3

print(sumThreeNums(3,3,3))
#%% Ex22

def oddOrEven(num):
    if num % 2 == 0 and num > 0:
        print("Number of {0} is even".format(num))
    elif num % 2 == 1 and num > 0:
        print("Number of {0} is odd".format(num))
    else:
        print("Number of {0} is zero or negative.".format(num))

oddOrEven(11)
#%% Ex23

def reversing(num):
    num = str(num)
    return num[::-1]

print(reversing(15684382))
#%% Ex24

def biggestAndSmallest(num1,num2,num3):
    if num1 < (num2 and num3):
        if num2 < num3:
            print("Biggest number is {0} and smallest number is {1}".format(num3,num1))
        else:
            print("Biggest number is {0} and smallest number is {1}".format(num2,num1))
    elif num2 < (num1 and num3):
        if num1 < num3:
            print("Biggest number is {0} and smallest number is {1}".format(num3,num2))
        else:
            print("Biggest number is {0} and smallest number is {1}".format(num1,num2))
    elif num3 < (num1 and num2):
        if num2 < num1:
            print("Biggest number is {0} and smallest number is {1}".format(num1,num3))
        else:
            print("Biggest number is {0} and smallest number is {1}".format(num2,num3))
    else:
        print("All equal to each other")

biggestAndSmallest(3,3,1)

num1 = 12
num2 = 21
num3 = 33

listOfNumbers = [num1,num2,num3]
print("The biggest number of the list is : {}".format(max(listOfNumbers)), "The smallest number of the list is : {}".format(min(listOfNumbers)))
#%% Ex25

n = int(input("Enter the number of elements in the list : "))
listOfNumbers = []

for i in range(n):
    num = int(input("Enter a number : "))
    listOfNumbers.append(num)
    
total = sum(listOfNumbers)
print(total)