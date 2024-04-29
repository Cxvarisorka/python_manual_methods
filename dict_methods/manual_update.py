def manual_update(main_dict, update_dict):
    result = {}

    for key in main_dict:
        result[key] = main_dict[key]

    for key in update_dict:
        result[key] = update_dict[key]

    return result

test = {
    "a": 1,
    "b": 2,
    "c": 3
}

print(manual_update(test, {"a": 2, "d": 4}))