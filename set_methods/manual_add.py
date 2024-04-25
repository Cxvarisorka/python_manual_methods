def manual_add(set_collection, value):
    set_collection = list(set_collection)
    set_collection.append(value)
    return set(set_collection)

print(manual_add({"Luka", 1, False}, "Mari"))