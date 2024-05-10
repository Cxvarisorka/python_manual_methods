def manual_pop(dict_collection, key_remove = None):
    result = {}
    if key_remove is None:
        keys = [key for key in dict_collection]
        key_remove = keys[-1]

    for key in dict_collection:
        if key != key_remove:
            result[key] = dict_collection[key]
            
    return result


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}


print(manual_pop(thisdict))