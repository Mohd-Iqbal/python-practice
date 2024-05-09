# from classes import Car

# car_1 = Car("Chevy","Corvette",2021,"blue")
# car_2 = Car("Ford","Mustang",2022,"red")

# in python for getting the attributes of the object created we can use vars function 
# attributes = vars(car_1)

# car_2.drive()
# car_1.stop()

# walrus operator
# The walrus operator (:=) is a relatively new addition to Python, introduced in Python 3.8. It is also known as the "assignment expression." The operator allows you to assign a value to a variable as part of an expression. It is particularly useful in while-loops and list comprehensions where you want to both compute a value and keep it for later use.

# Here's a simple example to demonstrate its use:
        
# # Without walrus operator
# n = 0
# while n < 5:
#     print(n)
#     n += 1

# # With walrus operator
# n = 0
# while (n := n + 1) < 5:
#     print(n)
        
# In the second example, the walrus operator := is used to both increment n and check if it's less than 5 within the while condition. This can make the code more concise and readable, especially in situations where you want to avoid duplicating expressions or computations.

# function to variable 

# def hello():
#     print("Hello iqbal!")

# hi = hello
# hi()

# Higher Order Function = a function that either:
#                         1. accepts a function as an argument 
#                            or 
#                         2. returns a function
#                         (in python, functions are also treated as objects)

# example 1

# def loud(text):
#     return text.upper()

# def quiet(text):
#     return text.lower()

# def hello(func):
#     text = func("Iqbal khan")
#     print(text)

# hello(loud)
# hello(quiet)

# example 2

# def divisor(x):
#     def dividend(y):
#         return y / x
#     return dividend

# divide = divisor(5)
# print(divide(10))

# Lambda function = function written in 1 line using lambda keyword accepts any number of arguments, but only has one expression. (think of it as a shortcut)
# (useful if needed for a short period of time, throw-away)
# lamda parameters:expression

# full_name = lambda first,last: first+" "+last
# adult = lambda age:True if age >= 18 else False
# print(adult(18))


# sort and sorted function: both are used to sort the iterables, sort is used only with list while sorted can be used with all iterables. sort returns nothing but modifies the original list while sorted returns new iterable with no modification in original iterable

# In Python, the sorted() and sort() functions can take a key argument, which is a function that is called on each element of the iterable that is being sorted. This function is used to extract a key from each element, and the elements are then sorted based on the keys.

# When you use a lambda function as the key argument for sorted(), you are essentially providing a custom way to extract a key from each element for the purpose of sorting. Here's a simple example to illustrate how this works:

# def sorting(x):
#     return x["age"]

# people = [
#     {'name': 'Alice', 'age': 30},
#     {'name': 'Bob', 'age': 25},
#     {'name': 'Charlie', 'age': 35}
# ]

# # Sort the list of dictionaries by age
# sorted_people = sorted(people, key=sorting, reverse=True)
# sorted_people = sorted(people, key=lambda x: x["age"], reverse=True)
# print(sorted_people)
# In this example, the lambda function lambda x: x['age'] is used as the key argument for sorted(). This lambda function takes each dictionary x from the people list and returns the value associated with the key 'age'. The sorted() function uses these extracted age values as the keys for sorting the people list, resulting in a sorted list of dictionaries based on the ages.


# map() = applies a function to each item in an iterable (list, tuple, etc.)
# map(function,iterable)

# store = [("shirt",20.00),
#          ("pants",25.00),
#          ("jacket",50.00),
#          ("socks",10.00)]

# new_store = list(map(lambda data: (data[0],data[1] * 0.82),store))
# print(new_store)

# filter() = creates a collection of elements from an iterable for which a function returns true 
# filter(function,iterable)

# store = [("shirt",20.00),
#          ("pants",25.00),
#          ("jacket",50.00),
#          ("socks",10.00)]

# new_store = list(filter(lambda data:data[1] > 20.00,store))
# print(new_store)

# reduce() = apply a function to an iterable and reduce it to a single cumulative value, performs function on first two elements and repeats process until 1 value remains
# reduce(function,iterable)

# import functools
# factoial = [5,4,3,2,1]
# fac_5 = functools.reduce(lambda x, y: x * y, factoial)
# print(fac_5)


# list comprehension = a way to create a new list with less syntax can mimic certain lambda functions, easier to read
# list = [expression for item in iterable]
# list = [expression for item in iterable if conditional] # using if condition with it
# list = [expression (if/else) for item in iterable] # using if/else condition with it

# students = [100,90,80,70,60,50,40,30,0]

# declaration = [i if i >= 60 else "failed" for i in students]

# print(declaration)

# digits = [1,2,3,4,5]

# tuple_sqaures = [(i,i*i) for i in digits]

# print(tuple_sqaures)

# dictionary comprehension = create dictionaries using an expression can replace for loops and certain lambda functions
# dictionary = {key: expression for (key,value) in iterable}
# dictionary = {key: expression for (key,value) in iterable if conditional}
# dictionary = {key: (if/else) for (key,value) in iterable}
# dictionary = {key: function(value) for (key,value) in iterable}

# cities_in_F = {"New York":32, "Boston":75, "Los Angeles": 100, "Chicago": 50}
# cities_in_C = {key: round((value - 32)*(5/9)) for (key,value) in cities_in_F.items()}
# print(cities_in_C)

# weather = {"New York":"snowing", "Boston":"sunny", "Los Angeles": "sunny", "Chicago": "cloudy"}
# using filter vs dictionary comprehention
# filtered = dict(filter(lambda items: items[1] == "sunny",weather.items()))
# weather_sunny = {key: value for (key,value) in weather.items() if value == "sunny"}
# print(weather_sunny)

# cities_in_F = {"New York":32, "Boston":75, "Los Angeles": 100, "Chicago": 50}
# cities_weather = {key: ("warm" if value >= 50 else "cold") for (key,value) in cities_in_F.items()}
# print(cities_weather)

# def check_temp(value):
#     if value >= 70:
#         return "hot"
#     elif 69 >= value >= 40:
#         return "warm"
#     else:
#         return "cold"
    
# cities_in_F = {"New York":32, "Boston":75, "Los Angeles": 100, "Chicago": 50}
# cities_weather = {key: check_temp(value) for (key,value) in cities_in_F.items()}
# print(cities_weather)


# zip(*iterables) = aggregate elements from two or more iterables (list,tuple,sets,etc.)
# creates a zip object with paired elements stored in tuple for each element

# note: When using the zip function in Python, the length of the input iterables must be the same. If the iterables are of different lengths, zip will stop generating tuples as soon as the shortest input iterable is exhausted. 

# usernames = ["khalid","Jamal","Ubaid"]
# passords = ("password", "guest", "tittles")
# login_date = [2012,2014,2022]

# users = zip(usernames,passords,login_date)

# for i in users:
#     print(i)

# if __name__ == "__main__"

# The if __name__ == "__main__" construct is a common idiom used in Python scripts to differentiate between being run as a standalone program or being imported as a module into another script. This construct is particularly useful when you have code in a Python file that should only run when the file is executed directly, not when it is imported into another script.

# Here's how it works:
# When a Python file is executed, Python sets a special variable called __name__ to have a value of "__main__".
# When a Python file is imported as a module into another script, the __name__ variable is set to the name of the module (i.e., the filename without the .py extension), not "__main__".
# By using if __name__ == "__main__", you can ensure that certain code only runs when the script is executed directly, not when it is imported. This is commonly used for including test code or setup code that should only run when the script is run standalone.

# Here's a simple example to illustrate:
# my_module.py
# def my_function():
#     print("Hello from my_function!")

# if __name__ == "__main__":
#     print("This will only run when my_module.py is executed directly, not when it is imported.")
#     my_function()

# When you run my_module.py directly, you will see the output:
# This will only run when my_module.py is executed directly, not when it is imported.
# Hello from my_function!


# However, if you were to import my_module into another script, the code inside the if __name__ == "__main__" block would not run, and you would not see the message.

# This construct is a best practice in Python programming because it allows you to write code that can be both imported and executed as a standalone script without causing unintended side effects.

# time module in python
# import time
# epoch = a date and time from which a computer measures system time 
# print(time.ctime(0)) # convert a time expressed in seconds since epoch to a readable string
# print(time.time()) # return current seconds since epoch

# one way of getting current date and time
# print(time.ctime(time.time())) 

# second way of getting current date and time
# time_object = time.localtime() # this returns an object time which is in inreadable format 
# local_time = time.strftime("%B %d %Y %H:%M:%S" ,time_object) # we use this to change the format of object time and it takes to arguments format and time object, for format we can refer to official python documentation, we can provide as many format directive as we want 
# print(local_time)

# time_object = time.gmtime() # getting UTC time

# time_string = "13 March, 2015"
# time_object = time.strptime(time_string,"%d %B,%Y") # for changing string time to time object

# change tuple time representation to time string
# (year, month, day, hours, minutes, seconds, #day of the week, #day of the year, dst)
# time_tuple = (2015, 6, 1, 7, 37, 12, 0, 0, 0)
# time_string =  time.asctime(time_tuple)
# print(time_string)

# change tuple time representation to seconds passed since epoch seconds
# time_string =  time.mktime(time_tuple)
# print(time_string)

# threading 
# thread = a flow of execution. Like a separate order of instructions. However each thread takes a turn running to achieve concurrency GLI = (global interpreter lock), allows only one thread to hold the control of the python interpreter

# cpu bound = program/task spends most of it's time waiting for internal events (CPU instensive) use multiprocessing
# io bound = program/task  spends most of it's time waiting for external events (user input, web scraping) use multithreading

# import threading
# import time

# for getting the number of total threads that are active or running
# print(threading.active_count())
# this gives us list of all the threads currently running 
# print(threading.enumerate())


# multithreading example
# let's say we are going to for exam and we have little time to do breakfast, coffee, and study, as humans we can do this multiple works simultaneaously. We can also achieve this in python through multithreading
# def breakfast():
#     time.sleep(4)
#     print("You finished breakfast")

# def coffee():
#     time.sleep(3)
#     print("You finished coffee")

# def study():
#     time.sleep(5)
#     print("You finished studying")

# if we use only our main thread then it will call these function sequentially if but we create three more threads for each taks then it won't wait for each other time to complete it's task rather it will run after it complete it's own time, here main thread will be responsible only for creating 3 threads
# threading.Thread(target=function, args=(arguments of the function)) # syntax of thread
# x = threading.Thread(target=breakfast)
# x.start()
# y = threading.Thread(target=coffee)
# y.start()
# z = threading.Thread(target=study)
# z.start()

# As main thread does not wait for other threads but we can make it wait for other threads before completing it's task 
# x.join()
# y.join()
# z.join()

# this provides us with time that main thread takes to complete it's task which in this case is creating 3 threads
# print(time.perf_counter())

# daemon threads = a thread that runs in the background, not important for program to run, your program will not wait for daemon threads to complete before exiting, not-deamon threads cannot normally be killed, stay alive until task is completed
# example background tasks, garbage collection, waiting for input, long running processes 

# we have created I program in which separate thread is created for timer function in which counter value increases after 1 second and checks that for how much time user was logged in when user answers if he want to exit 

# def timer():
#     print()
#     count = 0
#     while True:
#         time.sleep(1)
#         count += 1
#         print("logged in for:", count, "seconds")

# now if we create normal thread then it will keep execution until while loop becomes false which in this case will not become so we will create daemon thread which stops executing when the all other threads completed 

# 1 way of creating daemon thread
# x = threading.Thread(target=timer, daemon=True)

# 2 way of creating deamon thread 
# x = threading.Thread(target=timer)
# x.setDaemon(True)
# x.start()

# method for checking if thread is deamon or not 
# print(x.isDaemon())

# answer = input("Do you wish to exit?")

# multiprocessing = running tasks in parallel on different cpu cores, bypass GIL used for threading
                    # multiprocessing = better for cpu bound tasks (heavy cpu usage)
                    # multiprocessing = better for io bound tasks (waiting around)

from multiprocessing import Process, cpu_count
import time

def counter(num):
    count = 0
    while count < num:
        count += 1

def main():
    print(cpu_count())

    a = Process(target=counter, args=(250000000,))
    b = Process(target=counter, args=(250000000,))
    c = Process(target=counter, args=(250000000,))
    d = Process(target=counter, args=(250000000,))

    a.start()
    b.start()
    c.start()
    d.start()

    a.join()
    b.join()
    c.join()
    d.join()

    print("Finished in", time.perf_counter(), "seconds")

if __name__ == "__main__":
    main()