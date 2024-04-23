def manual_pop(collection, index_remove = -1):
    if index_remove < 0:
        index_remove = len(collection) + index_remove
    
    result = []
    
    for index in range(len(collection)):
        if index != index_remove:
            result.append(collection[index])
    
    return result

print(manual_pop(["Luka", "Lile", "Nia"], -3))