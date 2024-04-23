def manual_max(numbers_collection):
    min_number = numbers_collection[0]
    
    for number in numbers_collection:
        if min_number > number:
            min_number = number
    
    return min_number


print(manual_max([1,2,3,4,5]))


print()