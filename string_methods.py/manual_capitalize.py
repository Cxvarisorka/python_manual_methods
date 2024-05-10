def manual_capitalize(s):
    if not s:
        return s
    
    first_char = s[0]

    if 'a' <= first_char and first_char <= 'z':
        first_char = chr(ord(first_char) - ord('a') + ord('A'))
    
    return first_char + s[1:]


print(manual_capitalize('1uka'))