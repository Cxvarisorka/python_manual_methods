def manual_items(dict_collection):
    items = []
    for key in dict_collection:
        items.append((key, dict_collection[key]))
    return items

test = {
    "a": 1,
    "b": 2,
    "c": 3
}

print(manual_items(test))