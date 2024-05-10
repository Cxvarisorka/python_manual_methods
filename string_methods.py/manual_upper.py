def manual_upper(s):
    if not s:
        return s
    
    new_str = ''

    for char in s:
        if not ('A' <= char and char <= 'Z'):
            char = chr(ord(char) - 32)
        new_str += char
    
    return new_str

print(manual_upper('LuKAa'))