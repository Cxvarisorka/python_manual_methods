def manual_count(tuple_collection, item_to_count):
    count = 0

    for item in tuple_collection:
        if item == item_to_count:
            count += 1
    
    return count


print(manual_count((1,2,2,2,3,4), 2))