def manual_isdecimal(string):
    for char in string:
        if not ('0' <= char and char <= '9'):
            return False
    return True

name = "1223s"
print(manual_isdecimal(name))