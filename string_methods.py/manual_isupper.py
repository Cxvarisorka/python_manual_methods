def manual_isupper(string):
    for char in string:
        if not('A' <= char and char <= 'Z'):
            return False
    return True


print(manual_isupper('LUKA'))