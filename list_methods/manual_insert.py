def manual_insert(collection, item_insert, index_insert):
    if index_insert < 0:
        index_insert = len(collection) + index_insert
        
    result = []
    
    for index in range(len(collection)):
        if index == index_insert:
            result.append(item_insert)
            result.append(collection[index])
        else:
            result.append(collection[index])
    
    return result

print(manual_insert(["Luka", "lile", "nia"], "mari", -1))