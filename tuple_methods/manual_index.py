def manual_index(tuple_collection, item_find):
    for index in range(len(tuple_collection)):
        if tuple_collection[index] == item_find:
            return index

print(manual_index((1,2,3,4,5), 2))