def manual_index(collection, item_find, find_last = False):
    indexes = range(len(collection)) if not find_last else range(len(collection) - 1, -1, -1)
    for index in indexes:
        if collection[index] == item_find:
            return index
    return -1


numbers = [1,2,3,3,4,5,4,6,8,8,1,2,2]
print(manual_index(numbers, 2, True))
    
