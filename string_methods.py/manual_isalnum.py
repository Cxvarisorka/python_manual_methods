def manual_isdecimal(string):
    for char in string:
        if not ('0' <= char <= '9' or 'a' <= char.lower() <= 'z'):
            return False
    return True

name = "1223ssw"
print(manual_isdecimal(name))