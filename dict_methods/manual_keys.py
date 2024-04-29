def manual_keys(dict_collection):
    keys_list = []
    for key in dict_collection:
        keys_list.append(key)
    return keys_list


test = {
    "a": 1,
    "b": 2,
    "c": 3
}

print(manual_keys(test))