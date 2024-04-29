def manual_difference(main_set, *sub_sets):
    difference_set = set()

    for main_item in main_set:
        found = any(main_item in sub_set for sub_set in sub_sets)
        if not found:
            difference_set.add(main_item)
    
    return difference_set


set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}
set3 = {5, 6, 7, 8, 9}

print(manual_difference(set1, set2, set3)) 

print(manual_difference({"apple", "banana", "cherry"}, {"google", "microsoft", "apple"}, {"cherry", "micra", "bluebird"}))