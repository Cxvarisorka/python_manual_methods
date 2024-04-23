def manual_filter(func, collection):
    filtered_collection = []
    for item in collection:
        if func(item):
            filtered_collection.append(item)
    return filtered_collection


def positive(item):
    return item < 0

print(manual_filter(positive, [1, -2, 5, -5, -8, 2]))


print(list(filter(positive, [1, -2, 5, -5, -8, 2])))