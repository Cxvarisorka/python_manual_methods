names = ["Luka", "Nia", "Lile"] # lists are collection type, where we can store multiple values

print(names[1]) # lists are indexed, which means that each value has specific addres (index) and are ordered

print(names[-1]) # we can use negative indexes, len(names) - 1 == -1

print(names[0:2])  # slicing allows you to get multiple values from list

names.append("Mari") # append method is for to add new value into the list

# we can use for loops to loop over list
for name in names:
    print(name)

# loop over means our name variable will be each value from list