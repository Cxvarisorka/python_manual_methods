def manual_add(set_collection, value):
    return set(list(set_collection) + list((value, )))

names = {"Luka", "lile", "nia"}

print(manual_add(names, "mari"))