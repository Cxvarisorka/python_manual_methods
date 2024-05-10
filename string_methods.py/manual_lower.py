def manual_lower(s):
    if not s:
        return s
    
    new_str = ''

    for char in s:
        if not ('a' <= char and char <= 'z'):
            char = chr(ord(char) + 32)
        new_str += char
    
    return new_str

print(manual_lower('LuKAa,f'))