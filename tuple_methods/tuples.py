# Tuples are used to store multiple items in a single variable.

# Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.

# A tuple is a collection which is ordered and unchangeable.

# Tuples are written with round brackets.

names = ("Luka", "Lile", "Nia")

print(names[0]) # tuple is indexed

# names[0] = "Mari" # this will be error, because tuple is unchangeable

# We can change tuples but we need to use other tools

names = list(names) # we need to convert tuple to list using list() constructor

# we know that lists are changeable, so we can add or remove value

names.append("Mari")
names.remove("Luka")

names = tuple(names) # after we change list we can convert it back to tuple using tuple() constructor

# Also we can uncpack our items from tuple

(sister_1, sister_2, friends) = names

print(sister_1, sister_2, friends)

(sister_1, *friends) = names

print(friends)

# we can loop over tuple because it is ordered and indexed collection

for name in names:
    print(name)


print(len(names)) # we can know how many items are in tuple using len() function