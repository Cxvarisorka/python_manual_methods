def manual_swapcase(string):
    result = ''
    for char in string:
        if char.isupper():
            result += char.lower()
        else:
            result += char.upper()
    return result

print(manual_swapcase('luka var Me'))