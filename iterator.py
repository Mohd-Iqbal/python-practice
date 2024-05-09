# mytuple = ("apple", "banana", "cherry")
# myit = iter(mytuple)
# for i in myit:
#     print(i)

# # creating range function using iterator
# # this Range class is iterable 
# class Range:

#     def __init__(self,start,end) -> None:
#         self.start = start
#         self.end = end

#     def __iter__(self):
#         return Iterator(self)
    
# # this Iterator class is Iterator 
# class Iterator:

#     def __init__(self,iterable_obj) -> None:
#         self.obj = iterable_obj

#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         if self.obj.start >= self.obj.end:
#             raise StopIteration
        
#         current = self.obj.start
#         self.obj.start += 1
#         return current
    

# for i in Range(0,5):
#     print(i)

# range = Range(0,5)
# iterator = range.__iter__()
# print(iterator.__next__())
# print(iterator.__next__())
# print(iterator.__next__())
# print(iterator.__next__())
# print(iterator.__next__())


# Generators: an easy way to create iterators
# def generator():

    # yield "hello"
    # yield "hi"
    # yield "Iqbal"

# gen_obj = generator()

# for i in gen_obj:
#     print(i)

# print(gen_obj.__next__())
# print(gen_obj.__next__())
# print(gen_obj.__next__())


# generator expression 
# gen = (i**2 for i in range(1,11))
# for i in gen:
    # print(i)

# pascal traingle
# def pascal(times):
#     arr2 = [1]
#     yield [1]
#     arr1 = []
#     for _ in range(times):
#         num1 = 0
#         num2 = 1
#         for k in range(0,len(arr2)+1):
#             if k == 0:
#                 arr1.append(1)
#             elif k != len(arr2):
#                 arr1.append(arr2[num1]+arr2[num2])
#                 num1 += 1
#                 num2 += 1
#             else:
#                 arr1.append(1)
#         arr2 = arr1
#         yield arr1
#         num1 = 0
#         num2 = 1
#         arr1 = []

# for i in pascal(9):
#     print(i)

# anagram checker
def check_anagram(str1,str2):
    anagram = True

    if len(str1) != len(str2):
        return False

    for i in str1:
        if i not in str2:    
            anagram = False
    
    return anagram

print(check_anagram("fbsda","absdf"))