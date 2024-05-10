def manual_islower(string):
    for char in string:
        if not('a' <= char and char <= 'z'):
            return False
    return True


print(manual_islower('laka'))