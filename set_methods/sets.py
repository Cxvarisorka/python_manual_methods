# Sets are used to store multiple items in a single variable.

# Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.

# A set is a collection which is unordered, unchangeable*, and unindexed.


# Note: Set items are unchangeable, but you can remove items and add new items.

# Sets are written with curly brackets.

fruits = {"apple", "banana", "cherry"}

# Note: Sets are unordered, so you cannot be sure in which order the items will appear.

# print(fruits[0]) sets are unindexed this means we cant use indexes

# Set items are unordered, unchangeable, and do not allow duplicate values.

# Unordered
# Unordered means that the items in a set do not have a defined order.

# Set items can appear in a different order every time you use them, and cannot be referred to by index or key.

# Unchangeable
# Set items are unchangeable, meaning that we cannot change the items after the set has been created.

# Once a set is created, you cannot change its items, but you can remove items and add new items.

# Duplicates Not Allowed
# Sets cannot have two items with the same value.


# Get the length of a Set using len() function

print(len(fruits))

# We can loop over set

for fruit in fruits:
    print(fruit)

# we can add element to set

fruits.add("Orange")

print(fruits)

# To add items from another set into the current set, use the update() method.

# tropical = {"pineapple", "mango", "papaya", "apple"}

# fruits.update(tropical)

# print(fruits)

# The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).


tropical = ["pineapple", "mango", "papaya", "apple"]

fruits.update(tropical)

print(fruits)

# To remove an item in a set, use the remove(), or the discard() method.

fruits.remove("apple")

print(fruits)

# Note: If the item to remove does not exist, remove() will raise an error.

# Remove "banana" by using the discard() method:

fruits.discard("mango")

print(fruits)

# Note: If the item to remove does not exist, discard() will NOT raise an error.

# You can also use the pop() method to remove an item, but this method will remove a random item, so you cannot be sure what item that gets removed.

# The return value of the pop() method is the removed item.

removed_item = fruits.pop()

print(removed_item)
print(fruits)