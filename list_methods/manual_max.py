def manual_max(numbers_collection):
    max_number = numbers_collection[0]
    
    for number in numbers_collection:
        if max_number < number:
            max_number = number
    
    return max_number


print(manual_max([1,2,3,4,5]))