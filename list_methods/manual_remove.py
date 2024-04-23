def manual_remove(collection, delete_item):
    filtered_list = []
    
    for index in range(len(collection)):
        if collection[index] != delete_item:
            filtered_list.append(collection[index])
        else:
            filtered_list.extend(collection[index + 1:len(collection)])
            break
    
    return filtered_list