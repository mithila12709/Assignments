# 1.Write a Python program to print "Hello Python"?

print("Hello")

# 2.Write a Python program to do arithmetical operations addition and division.?

a=72
b=8
print (a+b)
print(a/b)

# Function:
def sum(a,b):
   return a+b

s=sum(56,89)
print(s)

#3.Write a Python program to find the area of a triangle?

b= 7
h=8
A = 0.5* (b * h)
print(A)

# 4. Write a Python program to swap two variables?

list = [8,9,5,6,7]
def swap(list):
   list[0],list[-1]=list[-1],list[0]
   return list

obj=swap(list)
print(obj)

#5.	Write a Python program to generate a random number?

import random

randint= random.randint(1,10)
print(randint)

#6.	Write a Python program to convert kilometres to miles?

def convert(kilo):
   return kilo *  0.62137

obj1=convert(12)
print(obj1)

# 7.Write a Python program to convert Celsius to Fahrenheit?

def convert1(cel):
   return ((cel * 9/5) + 32) 

objjj= convert1(32)
print(objjj)

#8.	Write a Python program to display calendar?

import calendar
year= 2024
month=2
print(calendar.month(year,month))

# we Can take input from the user also:
yy=int(input("Enter year: "))
mm=int(input("Enter month: "))

print(calendar.month(yy,mm))

#11. Write a Python Program to Check if a Number is Positive, Negative or Zero?

num=int(input("Enter a number: "))
if num>0:
   print("positive number")

elif num== 0:
   print("This is Zero")

else:
   print("Negative number")

#12.Write a Python Program to Check if a Number is Odd or Even?

num=int(input("Enter a number: "))
if num %2 == 0:
   print("Its a even number")
else:
   print("Its a Odd number")

#13	Write a Python Program to Check Leap Year?

year=int(input("Enter a year: "))

if (year %400 == 0 and year %100 == 00):
   print(f"{year} is a leap year")
elif (year %4 == 0 and year %100 != 0):
   print(f"{year} is a leap year ")
else:
   print("this is not a leap year")

#14.	Write a Python Program to Check Prime Number?
   
number= 11
for i in range (2,number):
   if number%i == 0:
      print("Not Prime")
   else:
      print("Prime Number")
      break
     

# By user:
num= int(input("Enter a number: "))

if num == 1:
   print("Its not a prime number")
if num>1:
   for i in range(2,num):
      if num%i == 0:
         print("Not a prime number")
         break  
   else:
     print("Prime number")


#15.Write a Python Program to Print all Prime Numbers in an Interval of 1-10000?

for num in range(0,101):
   if num>1:
      for i in range(2,num):
         if num%i == 0:
            break
      
      else:
         print(num)
      

#16.Write a Python Program to Find the Factorial of a Number?

def factorial(n):
    factorial = 1
    for i in range(n):
        factorial= factorial * (i+1)
    return factorial

fact=factorial(5)
print(fact)

#17.Write a Python Program to Display the multiplication Table?

num=int(input("Enter a number: "))
t=[num*i for i  in range (1,11)]
print(t)

# print table in dictionary:
{i:[i*j for j in range(1,11)] for i in range(2,6)}

#21.Write a Python Program to Find the Sum of Natural Numbers?

def sum(num1,num2):
   return num1+num2

s=sum(56,78)
print(s)

# 22.	Write a Python Program to Find LCM?

num1= int(input("Enter a first number: "))
num2= int(input("Enter a second number: "))  

max_num = max(num1,num2)

while (True):
   if max_num% num1 == 0 and max_num% num2==0:
      break
   max_num = max_num + 1

print(f"The LCM of {num1} and {num2} is {max_num}")

#23.Write a Python Program to Find HCF?

num1= int(input("Enter 1st num: "))
num2=int(input("Enter 2nd num: "))

min_num= min(num1,num2)

for i in range(1,min_num+1):
   if num1%i ==0 and num2%i ==0:
      hcf =i

print(f"The HCF of 2 numbers is {hcf}")

# 24.	Write a Python Program to Convert Decimal to Binary.

def convertbinary(n):
   if n > 1:
      convertbinary(n//2)
   print(n%2, end="")

convertbinary(15)

#25.	Write a Python Program To Find ASCII value of a character?

char="a"
print("The Value of ASCII is", ord(char))







