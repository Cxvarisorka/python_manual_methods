def find_item(func, collection, find_last = False):
    indexes = range(len(collection)) if not find_last else range(len(collection) - 1, -1, -1)
    for index in indexes:
        if func(collection[index]):
            return [collection[index], index]
    return -1


names = ["Luka", "Mari", "Mari", "Lile", "Nia"]


print(find_item(lambda name: len(name) == 3, names))