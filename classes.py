# in python this is better practice to create class in separate file and then import it, if classes are big 
class Car:

# this __init__ fucntion is constructor function which let's us to create an object of the class
# here this self refers to the object that we are creating
    def __init__(self,make,model,year,color):
        # these are the attributes of the objects that would be created using this class 
        self.make = make
        self.model = model
        self.year = year
        self.color = color

# these are the methods of the objects 
    def drive(self):
        print("This "+self.model+" is driving")

    def stop(self):
        print("This "+self.model+" is stopped")


# difference between class variable and instance variable 
# Class Variables: These variables are shared among all instances of a class. They are defined within the class but outside of any methods. Class variables are accessed using the class name. They are useful for defining properties that are common to all instances of the class. If you change the value of a class variable, all instances of the class will see the updated value.
# Example:
# class MyClass:
#     class_variable = 10

# obj1 = MyClass()
# obj2 = MyClass()

# print(obj1.class_variable)  # Output: 10
# print(obj2.class_variable)  # Output: 10

# MyClass.class_variable = 20

# print(obj1.class_variable)  # Output: 20
# print(obj2.class_variable)  # Output: 20
        
# Instance Variables: These variables are unique to each instance of a class. They are defined inside the __init__ method or any other method of the class. Instance variables are accessed using the instance name (self). Each instance can have different values for its instance variables.

# Example:
# class MyClass:
#     def __init__(self, instance_variable):
#         self.instance_variable = instance_variable

# obj1 = MyClass(10)
# obj2 = MyClass(20)

# print(obj1.instance_variable)  # Output: 10
# print(obj2.instance_variable)  # Output: 20

# uses of class variables      
# The use of class variables versus instance variables depends on the specific requirements of your program and the design you're aiming for. Here are some considerations:

# Shared State: Class variables can be useful when you want to maintain shared state among all instances of a class. For example, if you have a counter that needs to be incremented each time a new instance is created, a class variable would be appropriate.

# Default Values: Class variables can serve as default values that can be overridden by instance variables if needed. This can be useful when most instances should have a common default value, but some instances need a different value.

# Code Clarity: Using class variables can make the code more readable and maintainable by clearly indicating that certain properties are shared among all instances.

# Performance: Accessing class variables can be slightly faster than instance variables since Python does not have to look up the instance's dictionary. However, the performance difference is usually negligible unless you're working with a very large number of instances.
    
# inheritance = is concept in which child classes inherits all the attributes and methods of parent class       
# class Animal:

#     alive = True

#     def __init__(self,animal_name):
#         self.animal_name = animal_name

#     def eat(self):
#         print("This "+self.animal_name+" is eating")

#     def sleep(self):
#         print("This "+self.animal_name+" is sleeping")

# # we write child class like this 
# class Fish(Animal):
#     def swim(self):
#         print("This animal can swim")

# class Rabbit(Animal):
#     def run(self):
#         print("This animal can run")

# class Hawk(Animal):
#     def fly(self):
#         print("This animal can fly")

# fish = Fish("fish")
# rabbit = Rabbit("rabbit")
# hawk = Hawk("hawk")

# fish.swim()
# rabbit.run()
# hawk.fly()
# print(hawk.alive)
# print(rabbit.animal_name)
# fish.eat()
# hawk.sleep()

# # multi-level inheritance = when a derived class (child) class inherits another derived class (child) class 
# class Organism:

#     alive = True

# class Animal(Organism):

#     def eat(self):
#         print("Animal is eating")

# class Dog(Animal):

#     def bark(self):
#         print("dog is barking")

# dog = Dog()
# print(dog.alive) # inherited from the Organism class
# dog.eat() # inherited from the Animal class
# dog.bark() # defined in Dog class
        
# multiple inheritance = when a child class is derived from more than one parent class 

# class Prey:

#     def flee(self):
#         print("This animal flees")

# class Predator:

#     def hunt(self):
#         print("This animal hunts")

# class Rabbit(Prey):
#     pass
# class Hawk(Predator):
#     pass
# class Fish(Prey,Predator):
#     pass
    
# rabbit = Rabbit()
# hawk = Hawk()
# fish = Fish()

# rabbit.flee()
# hawk.hunt()
# fish.flee()
# fish.hunt()
        
# method overriding 
# Overriding methods permit a user to change the existing methods’ behaviour. For its implementation, a minimum of two classes are needed.
# The key benefit is that it allows the main class to declare those methods shared by all. Also, it allows subclasses to define their implementations of any or all such methods.
# When overriding a method, you need to use inheritance.
# The parent class function and child class function must have the same signature. They must have the same number of parameters.
# It allows a child class to adapt the execution of any method provided by any one of its parent classes.
        
# class Animal:

#     def eat(self):
#         print("This animal is eating")

# class Rabbit(Animal):

#     def eat(self):
#         print("This rabbit is eating a carrot")

# rabbit = Rabbit()
# rabbit.eat()
        
# method chaining = calling multiple methods sequentially each call performs an action on the same object and returns self

class Car:

    def turn_on(self):
        print("You start the engine")
        return self

    def drive(self):
        print("You drive the car")
        return self

    def brake(self):
        print("You step on the brake")
        return self

    def turn_off(self):
        print("You turn off the engine")
        return self
    
# in method chaining we return self so that the returned self should be used to call another method of it 
    
car = Car()

# car.drive().turn_off()

car.turn_off().turn_on().brake().turn_off()

# a more beautiful way of writing above chaining is to use backslash (\) which represents line continuation
# car.turn_on()\
#    .drive()\
#    .brake()\
#    .turn_off()
        
# super() = function used to give access to the methods of a parent class. Returns a temporary object of a parent class whne used
        
# class Shape:

#     def __init__(self, length, width):
#         self.length = length
#         self.width = width

# class Square(Shape):

#     def __init__(self, length, width):
#         super().__init__(length, width)

#     def area(self):
#         return self.length*self.width
    
# class Cube(Shape):

#     def __init__(self, length, width, height):
#         super().__init__(length, width)
#         self.height = height

#     def area(self):
#         return self.length*self.width*self.height
    

# square = Square(5,5)
# cube = Cube(5,5,5)

# print(square.area())
# print(cube.area())
        
# abstract class 
# prevents a user form creating object from that class, compels the user to override abstract methods in a child class 
    
# abstract class = a class which contains one or more abstract methods. 
# abstract methods = a method that has a declaration but does not have an implementation 
        
# here we have program in which we will prevent the user to create object from the Vehical parent class because the vehical can be a 4 wheeler or 2 wheeler so we will compel them to create objects from Car or Motorcycle class 
        
# Note: abstract classes behaviour same as normal class like we can use its methods in child class only thing we can't do with it is creating objects of it directly 
        
# uses of abstract classes 
# Creating a Template: Abstract classes can define a template for a group of subclasses. They can provide default implementations for some methods while leaving others abstract, allowing subclasses to provide their own implementations for the abstract methods.

# Enforcing a Contract: Abstract classes can define a contract that subclasses must adhere to. This helps ensure that subclasses provide specific functionality, which can be useful in frameworks or libraries where certain behaviors are expected.

# Code Reuse: Abstract classes can be used to define common functionality that can be reused across multiple subclasses. By providing a common base class, you can avoid duplicating code in each subclass.

# Polymorphism: Abstract classes can be used to achieve polymorphism, where different subclasses can be treated interchangeably based on their common interface defined by the abstract class. This allows for more flexible and extensible code.

# API Design: Abstract classes can be used to design APIs where certain methods are required to be implemented by subclasses. This helps in creating a clear and consistent API for users of the class hierarchy.

# from abc import ABC, abstractmethod

# class Vehical(ABC):

#     @abstractmethod
#     def go(self):
#         pass

# class Car(Vehical):

#     def go(self):
#         print("You drive the car")

# class Motorcycle(Vehical):

#     def go(self):
#         print("You ride the motorcycle")

# car =  Car()
# motorcycle =  Motorcycle()

# car.go()

# objects as arguments 
# In Python, you can pass objects (instances of classes) as arguments to functions or methods. When you pass an object as an argument, you are passing a reference to the object, not a copy of the object itself. This means that if you modify the object within the function or method, the changes will affect the original object outside the function or method as well.
# Here's a simple example to illustrate passing objects as arguments:
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# def update_age(person_obj, new_age):
#     person_obj.age = new_age

# # Creating a Person object
# person = Person("Alice", 30)

# print("Before update:", person.age)  # Output: Before update: 30

# # Passing the Person object to the function
# update_age(person, 35)

# print("After update:", person.age)  # Output: After update: 35
        
# Duck typing = concept where the class of an object is less important than the method/attributes that class might have, class type is not checked if minimum methods/attributes are present. 
# "If it looks like a duck, swims like a duck, and quacks like a duck, then it probably is a duck"
        
# In Python, you can use duck typing in a flexible way where you don't necessarily need to pass the class itself to a function. Instead, you can pass instances of different classes that have the same method names and signatures, and the function will work with them as long as they support those methods.
# For example:
        
# class Duck:
#     def quack(self):
#         print("Quack!")

# class Person:
#     def quack(self):
#         print("I'm quacking like a duck!")

# # Function that takes any object that has a 'quack' method
# def make_sound(obj):
#     obj.quack()

# # Using duck typing with instances
# duck = Duck()
# person = Person()

# make_sound(duck)    # Output: Quack!
# make_sound(person)  # Output: I'm quacking like a duck!

# In this example, the make_sound function can accept instances of both the Duck and Person classes without needing to change the function definition or parameter name. As long as the objects passed to make_sound have a quack method, the function will work correctly. This flexibility is one of the strengths of duck typing in Python.
        
