def manual_count(collection, count_item):
    count = 0
    
    for item in collection:
        if count_item == item:
            count += 1
    
    return count

print(manual_count("Lukkaa", "a"))