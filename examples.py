print("Hello, World!")

import sys

print(sys.version)

if 5 > 2:
  print("Five is greater than two!")


if 5 > 2:
 print("Five is greater than two!") 
if 5 > 2:
        print("Five is greater than two!") 


#This is a comment.
print("Hello, World!")


print("Hello, World!") #This is a comment

#print("Hello, World!")
print("Cheers, Mate!")

#This is a comment
#written in
#more than just one line
print("Hello, World!")


"""
This is a comment
written in
more than just one line
"""
print("Hello, World!")



x = 5
y = "John"
print(x)
print(y)


x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)


x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0


x = 5
y = "John"
print(type(x))
print(type(y))



x = "John"
# is the same as
x = 'John'

a = 4
A = "Sally"
#A will not overwrite a


myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

x = y = z = "Orange"
print(x)
print(y)
print(z)

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)


x = "Python is awesome"
print(x)



x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

x = "Python "
y = "is "
z = "awesome"
print(x + y + z)


x = 5
y = 10
print(x + y)


x = 5
y = "John"
print(x, y)


x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)


def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)


x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)


x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3

x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'



b = "Hello, World!"
print(b[2:5])