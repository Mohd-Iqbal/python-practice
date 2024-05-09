# string = "HelloMyNameIsKhan"

# string = "".join(
#     [i if i.islower() else " " + i.lower() if i in ["N","I"]  else " " + i for i in string]
#     )[1:]

# print(string)

# prime numbers tell 100
# numbers  = [i for i in range(2,100) if all(i % j != 0 for j in range(2,int(i**0.5) + 1))]
# print(numbers)

# matrix transpose
# matrix = [[1, 2, 3],
#           [4, 5, 6],
#           [7, 8, 9]]
# matrix = [[matrix[i][k] for i in range(len(matrix))] for k in range(len(matrix))]
# print(matrix)

# string = "Iqbal"
# string = "".join([
#     string[i] for i in range(len(string)-1,-1,-1)
# ])
# print(string)

# dict1 = {'a': 1, 'b': 2, 'c': 3}
# dict2 = {'b': 2, 'c': 4, 'd': 5}

# dictionary1 =  {key:dict1[key] for key in dict1 if key in dict2 and dict1[key] == dict2[key]}
# print(dictionary1)

# list_keys = [i for i in dict1.keys()] + [i for i in dict2.keys() if i not in dict1]
# dictionary2 = {key:(dict1[key] if key in dict1 and key not in dict2
                    # else dict2[key] if key in dict2 and key not in dict1 else [dict1[key],dict2[key]]) for key in list_keys}
# print(dictionary2)

# nested_dict = {
#     'key1': 1,
#     'key2': {
#         'key3': 3,
#         'key4': {
#             'key5': 5
#         }
#     },
#     'key6': {
#         'key7': 7
#     }
# }

# dictionary3 = {outer_key+"_"+inner_key+"_"+key: value
#                for (outer_key,inner_value) in nested_dict.items() 
#                for (inner_key,in_value) in (inner_value.items() if isinstance(inner_value,dict) else [("",inner_value)]) 
#                for (key,value) in (in_value.items() if isinstance(in_value,dict) else [("",in_value)])}
# print(dictionary3)


# data = [
#     ('a', 1),
#     ('b', 2),
#     ('a', 3),
#     ('c', 4),
#     ('b', 5)
# ]


# grouped_dict = {key: [value for k, value in data if k == key] for key, _ in data}
# print(grouped_dict)


# data = {
#     'apple': 1,
#     'banana': 2,
#     'orange': 3,
#     'kiwi': 4
# }

# dict = {key:value for key,value in data.items() if len(key) <= 5}
# print(dict) 


# palindrome
from string import punctuation

def palindrome(string):
    palindrome = True
    string = ''.join(char for char in string if char not in punctuation + ' ')
    lenght = len(string)
    halve = lenght // 2

    list1 = [string[i].lower() for i in range(0,halve)]
    list2 = [string[i].lower() for i in range(lenght-1,halve-1,-1)]

    for i in range(len(list1)):
        if list1[i] != list2[i]:
            palindrome = False
        
    return palindrome


string_palindrome = palindrome("A man, a plan, a canal, Panama.")
print(string_palindrome)