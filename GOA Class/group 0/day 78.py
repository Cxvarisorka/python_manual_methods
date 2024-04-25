# 1. Merge Lists: Write a function to merge two lists into a single list without any duplicates. For example, merging [1, 2, 3] and [3, 4, 5] should result in [1, 2, 3, 4, 5].

# list1 = [1,2,3]
# list2 = [3,4,5]

# merged_list = []

# for num in list1 + list2:
#     if num not in merged_list:
#         merged_list.append(num)

# print(merged_list)

# 2. List Comprehension: Create a list comprehension that squares each element of a given list. For instance, if the input list is [1, 2, 3, 4, 5], the output should be [1, 4, 9, 16, 25].

# Solution 1

# numbers_list = [1, 2, 3, 4, 5]
# squared_list = []

# for num in numbers_list:
#     squared_list.append(num ** 2)

# print(squared_list)

# Solution 2

# numbers_list = [1, 2, 3, 4, 5]
# squared_list = [num ** 2 for num in numbers_list]

# print(squared_list)

# 3. Filter Odd Numbers: Write a function that takes a list of integers as input and returns a new list containing only the odd numbers from the original list.

# Solution 1

# def filter_odd(numbers_list):
#     filtered_list = []

#     for number in numbers_list:
#         if number % 2 != 0:
#             filtered_list.append(number)
    
#     return filtered_list

# print(filter_odd([1,2,3,4,5]))

# Solution 2

# def filter_odd(numbers_list):
#     return [number for number in numbers_list if number % 2 != 0]

# numbers_list = [1,2,3,4,5]

# print(filter_odd(numbers_list))

# 4. Find Common Elements: Implement a function that takes two lists as input and returns a list containing the common elements between them

# Solution 1

# def find_commons(list1, list2):
#     common_items = []

#     for item in list1:
#         if item in list2:
#             common_items.append(item)
    
#     return common_items

# list1 = [1,2,3,4,5]
# list2 = [1,2,3]

# print(find_commons(list2, list1))

# Solution 2

# def find_commons(list1, list2):
#     return [number for number in list1 if number in list2]

# list1 = [1,2,3,4,5]
# list2 = [1,2,3,8,5,9]

# print(find_commons(list2, list1))

# 5. List Manipulation: Write a function to remove the duplicates from a given list while preserving the original order of elements. For example, if the input list is [1, 2, 3, 2, 4, 1], the output should be [1, 2, 3, 4]

# def remove_duplicates(list_collection):
#     filtered_list = []

#     for item in list_collection:
#         if item not in filtered_list:
#             filtered_list.append(item)
    
#     return filtered_list

# print(remove_duplicates([1, 2, 3, 2, 4, 1]))

# 6. Merge Dictionaries: Write a function to merge two dictionaries into a single dictionary. If there are overlapping keys, prioritize the values from the second dictionary. For example, merging {'a': 1, 'b': 2} and {'b': 3, 'c': 4} should result in {'a': 1, 'b': 3, 'c': 4}

# Solution 1

# def merge_dicts(dict1, dict2):
#     merged_dict = dict1.copy()
#     for key, value in dict2.items():
#         merged_dict[key] = value
#     return merged_dict

# dict1 = {"a": 1, "b": 2}
# dict2 = {"b": 3, "c": 4}
# print(merge_dicts(dict1, dict2))

# Solution 2

# def merge_dicts(dict1, dict2):
#     merged_dict = dict1.copy()
#     merged_dict.update(dict2)
#     return merged_dict
    

# dict1 = {"a": 1, "b": 2}
# dict2 = {"b": 3, "c": 4}

# print(merge_dicts(dict1, dict2))

# 7. Dictionary Comprehension: Create a dictionary comprehension that squares each value of a given dictionary. For instance, if the input dictionary is {'a': 1, 'b': 2, 'c': 3}, the output should be {'a': 1, 'b': 4, 'c': 9}

# Solution 1

# def square_dict(dict1):
#     new_dict = {}
#     for key, value in dict1.items():
#         new_dict[key] = value ** 2
#     return new_dict

# print(square_dict({'a': 1, 'b': 2, 'c': 3}))

# def square_dict(dict1):
#     return {key: value**2 for key, value in dict1.items()}

# print(square_dict({'a': 1, 'b': 2, 'c': 3}))

# 8. Dictionary Keys to List: Write a function that extracts all keys from a dictionary and returns them as a list. For example, if the input dictionary is {'a': 1, 'b': 2, 'c': 3}, the output should be ['a', 'b', 'c']

# Solution 1

# def extract_keys(dict1):
#     dict_keys = []

#     for key, value in dict1.items():
#         dict_keys.append(key)
    
#     return dict_keys

# print(extract_keys({'a': 1, 'b': 2, 'c': 3}))

# Solution 2

# def extract_keys(dict1):
#     return [key for key, _ in dict1.items()]

# print(extract_keys({'a': 1, 'b': 2, 'c': 3}))

# 9. Word Frequency Counter: Write a function that takes a string of text as input and returns a dictionary where keys are unique words in the text and values are the frequencies of those words

# Solution 1

# def word_counter(sentence):
#     result = {}
#     words = sentence.split(" ")

#     for word in words:
#         result[word] = words.count(word)

#     return result

# print(word_counter("luka luka tskhvaradze mari mari nia lile lile lile"))

# Solution 2

# def word_counter(sentence):
#     words = sentence.split(" ")
#     return {word: words.count(word) for word in words}

# print(word_counter("luka luka tskhvaradze mari mari nia lile lile lile"))
    
# 10. Dictionary Filtering by Value: Create a function that takes a dictionary and a value as input and returns a new dictionary containing only the key-value pairs where the value matches the input value.

# Solution 1

# def filter_dict(dict1, filter_value):
#     filtered_dict = {}

#     for key, value in dict1.items():
#         if value == filter_value:
#             filtered_dict[key] = value
    
#     return filtered_dict

# dict1 = {"a": 1, "b": 2, "c": 2, "d": 1, "e": 4}

# print(filter_dict(dict1, 1))

# Solution 2

# def filter_dict(dict1, filter_value):
#     return {key: value for key, value in dict1.items() if value == filter_value}

# dict1 = {"a": 1, "b": 2, "c": 2, "d": 1, "e": 4}

# print(filter_dict(dict1, 4))

# 11. Factorial Function: Write a function to compute the factorial of a non-negative integer. The factorial of a number n is the product of all positive integers less than or equal to n.

# Solution 1

# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n - 1)


# print(factorial(5))

