# variable has no type mentions like var let const in python simply write name of the variable like below and in python we mostly use Camel case like this first_name
# name = 'iqbal'

# for checking the data type 
# print(type(name))

# age = 3.5
# print(str(age) + " " + name)

# there are four basic data types in python string,integer,float,boolean. 

# multiple assignment = allows us to assign multiple variables at the same time in one line of code 

# name, age, attractive = "iqbal", 22, True 
# print(name, age, attractive)

# if we have multiple variables each with the same value so instead of assigning same value to it separately we can do like this 
# naveed = iqbal = bilal = sajjad = "afghan"

# print(naveed)
# print(iqbal)
# print(bilal)
# print(sajjad)

# string methods

# name = "iqbal"

# print(len(name))
# print(name.find("o"))
# print(name.capitalize())
# print(name.upper())
# print(name.lower())
# print(name.isdigit())
# print(name.isalpha())
# print(name.count("o"))
# print(name.replace("o", "a"))

# for writing multiple times 
# print(name*3)

# type casting = convert the data type of a value to another data type 

# age = 21
# print('age is '+ str(age))

# average = 5.8
# print(int(average))

# marks = "32.5"
# print(float(marks))

# user input in python

# name =  input("what is your name?: ")
# age = int(input("how old are you?: "))
# height = float(input("how tall are you?: "))

# print("hello "+ name)
# print("you are "+str(age)+" years old")
# print("you are "+str(height)+"cm tall")

# notes: 
# 1) in python user input is always in string so we have to change it to our desired data type through type casting 
# 2) python is sensitive to type of data type just like c, cpp

# math functions 

# import math

# pi = 3.14
# x = 4
# y = 2
# z = 8

# print(round(pi))
# print(math.ceil(pi))
# print(math.floor(pi))
# print(abs(pi))
# print(pow(pi,2))
# print(math.sqrt(9))
# print(max(x,y,z))
# print(min(x,y,z))

# slicing = create a substring by extracting elements from another string 
# indexing[] or slice()
# [start:stop:step]

# name = "Bro Code"

# this will create substring starting from index 0 to 2 
# first_name = name[0:3]
# it is the shortcut form of it where we don't specify the starting index python itself slice it from start 
# first_name = name[:3]

# this will create substring starting from index 4 to 7 
# first_name = name[4:8]
# it is the shortcut form of it where we don't specify the ending index python itself slice it from the given starting index till end
# first_name = name[4:]

# this will create substring starting from index 0 to 7 with leaving one character in between (default step is 1)
# funky_name = name[0:8:2]
# it is the shortcut form of it where we don't specify the starting and ending index python itself slice it from start to end with leaving 1 character in between 
# funky_name = name[::2]

# this reverses the string
# reversed_string = name[::-1]

# slice is same as indexing but we use comma instead colon

# website1 = "http://google.com"
# website2 = "http://wikipedia.com"

# minus indexing means that starting index count from right side or backwards
# slice = slice(7,-4)
# print(website1[slice]) # output => google
# print(website2[slice]) output => wikipedia

# if statements 

# age = 22

# if age >= 18:
#     print("your are a adult")
# else:
#     if age < 0:
#         print("you haven't been born yet")
#     else:
#         print("your are a child")

# if age >= 18:
#     print("your are adult")
# elif age < 0:
#     print("you haven't been born yet")
# else:
#     print("your are a child")

# logical operators

# temp = 10

# if temp >= 0 and temp <= 30:
#     print("the temprature is good today")
#     print("go outside")
# elif temp < 0 or temp > 30:
#     print("the temprature is bad today")
#     print("stay outside")

# if not(temp < 0 or temp > 30):
#     print("the temprature is good today")
#     print("go outside")
# elif  not(temp >= 0 and temp <= 30):
#     print("the temprature is bad today")
#     print("stay inside")

# for checking a value in iteratable data types like string, list, tuple etc we can use in keyword for it.

# drink = 'coffee'
# if "c" in drink:
#     print("present")

# loops 
# Use a for loop when you want to iterate over a sequence like a list, tuple, string, or range where you know the length or the elements you want to iterate over.
# Example: for i in range(5): will iterate 5 times, starting from 0 to 4.
# Use a while loop when you want to iterate until a certain condition is met, and the number of iterations is not known beforehand.
# Example: while x < 10: will continue to iterate as long as the condition x < 10 is true.

# this while loop will continue to run until user enters its name 

# name = None

# while not name:
#     name = input("Enter your name: ")

# print("Hello "+name)

# for i in range(10):
#     print(i + 1)
# computer starts counting from 0, so we add one to i in order to get values counting from 1 to 10  

# for i in range(50,100):
    # print(i)
# here counting will start from 50 to 99 because 100 is exclusive    

# for i in "iqbal":
    # print(i)
# for is used for every iteratable data

#program counting from 10 to 1 with 1 second wait and then print happy new year

# import time

# this third argument step is default 1 
# for seconds in range(10,0,-1):
#     print(seconds)
#     time.sleep(1)
# print("happy new year")

# nested loops  

# num1 = 1
# while num1 <= 5:
#     num2 = 1
#     while num2 <= 10:
#         print(num1 * num2)
#         num2 += 1
#     num1 += 1

# for i in range(10):
#     for i in range(10):
#         print("$", end="")
#     print()

# loop control statements = change a loops execution from its normal sequence

# break = used to terrminate the loop entirely 
# continue = skips to the next iteration of the loop 
# pass = does nothing, acts as a placeholder

# while True:
#     name = input("enter your name: ")
#     if name != "":
#         break

# phone_number = "123-456-7890"
# num = 0
# while num <= len(phone_number) - 1:
#     if phone_number[num] == "-":
#         num += 1
#         continue
#     print(phone_number[num])
#     num += 1

# for i in range(11):
#     if i == 5:
#         pass
#     else:
#       print(i)

# list = used to store multiple items in a single variable

# food = ["pizza","hamburger","hotdog","spaghetti"]

# food.append("roast")
# food.remove("hotdog")
# food.pop()
# food.insert(0,"cake")
# food.sort()

# print(food)

# 2D lists = a list of lists

# drinks = ["coffee","soda","tea"]
# dinner = ["pizza","hamburger","hotdog"]
# dessert = ["cake","ice cream"]

# food = [drinks,dinner,dessert]
# print(food[2][1]) 

# tuple = collection which is ordered and unchangeable used to group together related data 

# student = ("iqbal",21,"male")

# print(student.count("iqbal"))
# print(student.index("male"))

# for x in student:
#     print(x)

# if "iqbal" in student:
#     print("iqbal is present")

# Use tuples when:
# Immutability is needed: If you have a collection of items that should not change, use a tuple. For example, coordinates (x, y) or a database record with fixed fields.
# Performance is critical: Tuples are generally faster than lists because they are immutable. If you're working with a large dataset that doesn't need to change, tuples can be more efficient.
# Sequence unpacking: Tuples are useful for unpacking sequences into variables. For example, when returning multiple values from a function, you can return them as a tuple and unpack them outside the function.
# Dictionary keys: Since tuples are immutable, they can be used as keys in dictionaries, whereas lists cannot be used because they are mutable.
    
# Use lists when:
# Mutability is needed: If you need to add, remove, or modify elements in your collection, use a list.
# Dynamic length: Lists can grow or shrink in size as needed, making them suitable for situations where the number of elements is not fixed.
# Iteration and manipulation: Lists are more versatile for iterating over elements, modifying them, or using list-specific methods like append(), extend(), insert(), remove(), pop(), etc.
# Homogeneous data: If you have a collection of items that are all of the same type, lists are more commonly used and provide more flexibility in terms of operations you can perform on them.

# set = collection which is unordered, unindexed.No duplicate values

# utensils = {"fork","spoon","knife"}
# dishes = {"bowl","plate","cup","knife"}

# utensils.add("napkin")
# utensils.remove("fork")
# utensils.clear()
# dishes.update(utensils)
# newSet = dishes.union(utensils)
# newSet = dishes.intersection(utensils)
# newSet = dishes.difference(utensils)

# if "fork" in utensils:
#     print("present")

# for i in newSet:
#     print(i)

# dictionary = A changeable, unordered collection of unique key:value pairs, fast because they use hashing, allow us to access a value quickly

# capitals = {"Pakistan":"Islamabad",
#             "Afghanistan":"Kabul",
#             "Russia":"Moscow"}

# for updating existing key in two ways
# capitals["Russia"] = "London"
# capitals.update({"Russia":"Moscow"})

# for adding new key value to it 
# capitals.update({"Iran":"Tehran"})

# print(capitals)
# print(capitals["Russia"])
# get method is more save way of accessing a single key value
# print(capitals.get("Russia"))
# print(capitals.keys())
# print(capitals.values())
# print(capitals.items())
# print(capitals.pop("Pakistan"))
# print(capitals.clear())

# for key,value in capitals.items():
#     print(key,value)

# functions
# if we have funtion but don't want to have some code at the moment we can use pass keyword in it 

# def multiply(num1,num2):
    # return num1 * num2

# x = multiply(9,5)
# print(x)

# def hello():
#     pass

# hello()

# write a program which provides the max-length of subarray of binary array having same number of one and zero  

# array =  [0,1,1,0,1,0,1,0,0,0,0,1,1,0,1,1,1,0,1,0,1,0,0,0,1]

# sum = 0
# zero = 0
# one = 0

# for i in range(len(array)):
#     if array[i] == 0:
#         zero += 1
#     else:
#         one += 1
#     if one == zero:
#        sum = max(sum,one + zero)

# print(sum)

# keyword arguments = arguments preceded by an identifier when we pass them toa a function.The order of the arguments doesn't matter, unlike positional arguments Python knows the names of the arguments that our fucntion receives

# def hello(first,middle,last):
#     print("Hello "+first+" "+middle+" "+last)

# hello(middle="Iqbal",last="Seelab",first="Muhammad")


# LEGB is an acronym that stands for Local, Enclosing, Global, and Built-in, which are the four scopes in Python used for variable resolution. These scopes determine the order in which Python looks for variables when they are referenced in code.

# Local (L): This is the innermost scope, which includes variables defined within a function. When a function is called, Python first looks for the variable within the local scope. If the variable is not found here, Python moves to the next scope.

# Enclosing (E): This scope is used for nested functions. If a function is defined inside another function, the enclosing scope refers to the outer function's scope. Python searches for variables in this scope if they are not found in the local scope.

# Global (G): The global scope includes variables defined at the uppermost level of a script or module, outside of any function. If a variable is not found in the local or enclosing scope, Python looks for it in the global scope.

# Built-in (B): This is the outermost scope, which includes built-in functions and keywords provided by Python. If a variable is not found in any of the previous scopes, Python assumes it is a built-in name.

# args = parameter that will pack all the arguments into a tuple useful so that a function can accept a varying amount of arguments 

# problem is that we can pass only the specified amount of arguments to a function due to specified parameters, so we use args parameter which allow us to pass as many arguments as we can like 

# def add(*args):
    # sum = 0
    # args is tuple which is unchangeable so if we want to change the value of any parameter we can simply type cast tuple to a list and change value easily 
    # args = list(args)
    # args[0] = 23
    # for i in args:
        # sum += i
    # return sum

# print(add(3,7,1,5,8))

# kwargs = parameter that will pack all the arguments into a dictionary useful so that a function can accept a varying amount of keyword arguments 

# def hello(**kwargs):
#     print("hello", end=" ")
#     for key,value in kwargs.items():
#         print(value, end=" ")

# hello(title="Mr",first="Muhammad",middle="Iqbal",last="Seelab")

# str.format() = optional method that gives users more control when displaying output

animal = "cow"
item = "moon"

# print("The {} jumped over the {}".format("cow","moon"))
# print("The {} jumped over the {}".format(animal,item))

# we can position the arguments given through index 
# print("The {1} jumped over the {0}".format(animal,item)) positional arguments

# we can use the same index in all places
# print("The {0} jumped over the {0}".format(animal,item))

# we can use the keyword arguments
# print("The {animal} jumped over the {item}".format(animal="dog",item="earth"))

# we use same keyword multiple times 
# print("The {animal} jumped over the {animal}".format(animal="dog",item="earth"))

# add padding to string through format method

# just add ":" with value of number of spaces
# print("The {:12} jumped over the {}".format("cow","moon"))
# align to the left side 
# print("The {:<12} jumped over the {}".format("cow","moon"))
# align to the right side 
# print("The {:>12} jumped over the {}".format("cow","moon"))
# align to the center
# print("The {:^12} jumped over the {}".format("cow","moon"))
# using the keyword arguments 
# print("The {animal:^12} jumped over the {item}".format(item="cow",animal="moon"))

# formating with number using format method

# pi = 3.14563
# number = 1000

# for displaying only two number after point 
# print("The number pi is {:.2f}".format(pi))
# for adding comma at the thousand place
# print("The number is {:,}".format(number))
# for showing binary form of number
# print("The number is {:b}".format(number))
# for showing the octal form of number
# print("The number is {:o}".format(number))
# for showing the hexadecimal form of number
# print("The number is {:X}".format(number))
# to scientific notation 
# print("The number is {:E}".format(number))


# random module 
# import random

# x = random.randint(1,6) # generate random numbers from 1 to 6
# y = random.random() # generate random floating numbers between 0 and 1

# randomly choose item from the list 
# myList = ["rock","paper","scissors"]
# z = random.choice(myList)

# shuffles the list
# cards = [1,2,3,4,5,6,7,8,9,"J","Q","K","A"]
# random.shuffle(cards)

# print(cards)

# exception = events detected during execution that interrupt the flow of a program

# try:
#     numerator = int(input("Enter a number to divide: "))
#     denominator = int(input("Enter a number to divide by: "))
#     result = numerator / denominator
#     # either print result here or in else block if no exception present
# except ZeroDivisionError as e:
#     # we will first use those exception which we know that we can get it, and then only exception at the end if we miss any  
#     # as e prints us with what the exception is about
#     print(e)
#     print("You can't divide by zero idiot!")
# except ValueError as e:
#     print(e)
#     print("Enter only numbers plz")
# except Exception as e:
#     print(e)
#     print("Something went wrong : (")
# else:
#     print(result)
# finally:
#     # we most use this with files to close or open it 
#     print("This will always execute")

# file handling 
# import os

# checking file, folder/directory is present
# path = os.path.join(os.path.dirname(__file__),"test.txt")

# if os.path.exists(path):
#     print("That location exists")
#     if os.path.isfile(path):
#         print("That is a file")
#     elif os.path.isdir(path):
#         print("That is a directory")
# else:
#     print("That location doesn't exists")

# reading files 
# if file is present inside the same directory then only write file name with extention 
# if it is present in some another directory then write whole path
# with open('test.txt') as text:
#     print(text.read())

# normally when we read a file it is open and we have to close it manually but we write the program as with open then it automatically close it.
# print(text.closed)

# while with open can only close the file not catch any exception like not found exception so we use try except for exceptions

# try:
#     with open('test.txt') as file:
#      print(file.read())
# except FileNotFoundError:
#     print("That file was not found : (")

# writing to a file 

# text = "How are you?"

# second argument it takes is "r" for read and "w" for write "a" for append default is r 
# with open("test.txt","a") as file:
    # file.write(text)

# copying contents of file
# import shutil

# copyfile() = copies contents of a file 
# copy() = copyfile() + permission mode + destination can be a directory 
# copy2() = copy() + copies metadata (file's creation and modification times) 

# shutil.copyfile('test.txt','copy.txt') # src,dst 

# moving a file or directory to a different destination
# import os

# source = 'copy.txt'
# destination = "text.txt"

# try:
#     if os.path.exists(destination):
#         print("There is already a file there")
#     else:
#         os.replace(source,destination)
#         print(source+" was moved")
# except FileNotFoundError:
#     print(source+" wan not found")

# deleting file 
# import os
# import shutil
# path = "test.txt"

# this os.remove() method doesn't remove the empty folders so we use exception for that as well  

# try:
#     os.remove(path)
#     # for empty folder if it contains no files
#     # os.rmdir(path)
#     # for deleting folder with files 
#     # shutil.rmtree(path)
# except FileNotFoundError:
#     print("That file was not found!")
# except PermissionError:
#     print("You do not have permission to delete that")
# except OSError:
#     print("You cannot delete that using that function")
# else:
#     print(path+" was deleted")

# module = a file containing python code. May contain functions, classes, etc. used with modular programming which is to separate a program into parts 

# import messages 

# messages.hello()
# messages.bye()

# import messages as msg 

# msg.hello()
# msg.bye()

# from messages import hello,bye

# hello()
# bye()

# from messages import *

# hello()
# bye()

# list of all pre-built modules 
# help("modules")