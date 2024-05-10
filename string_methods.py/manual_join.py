def manual_join(string_list, join_char):
    result = ''
    for string in string_list:
        result += string + join_char
    
    return result[:-1]


print(manual_join(["luka", "lile", "Nia"], '-'))
