def manual_isalpha(s):
    if not s:
        return s
    
    for char in s:
        if not('a' <= char.lower() <= 'z'):
            return False
    
    return True


print(manual_isalpha('lu2'))