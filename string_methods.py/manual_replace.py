def manual_replace(string, replace_str, replace_chars):
    result = ''
    index = 0

    while index < len(string):
        if string[index:index + len(replace_str)] == replace_str:
            result += replace_chars
            index += len(replace_str)
        else:
            result += string[index]
            index += 1
    
    return result

name = "Luka Tskhvaradze"

print(manual_replace(name, 'a', 'ok'))