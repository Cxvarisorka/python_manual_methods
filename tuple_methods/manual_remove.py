def manual_remove(set_collection, value_to_remove):
    if value_to_remove not in set_collection:
        raise KeyError(f"'{value_to_remove}' not found in set")
    
    result = set({})
    for item in set_collection:
        if item != value_to_remove:
            result.add(item)
    return result


print(manual_remove({"Luka", "Lile", "Nia"}, "ger"))