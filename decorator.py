# import time 

# def cache(func):
#     cache_data = {}
#     print(cache_data)
#     def wrapper(*args,**kwargs):
#         if args in cache_data:
#             return cache_data[args]
#         result = func(*args,**kwargs)
#         cache_data[args] = result
#         return result 
#     return wrapper

# @cache
# def sum(a,b):
#     time.sleep(4)
#     adds = a + b
#     return adds

# print("inside", sum(4,5))
# print("inside", sum(4,5))


# def cache(func):
#     def wrapper(*args,**kwargs):
#         func(*args,**kwargs)
#     return wrapper

# @cache
# def hello():
#     print("hello")

# hello()