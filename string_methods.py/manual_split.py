def manual_split(str, split_char = ''):
    splited_str = []
    word = ''
    str += split_char

    for char in str:
        if split_char != char:
            word += char
        else:
            splited_str.append(word)
            word = ''
    
    return splited_str

fullname = "Luka Tskhvaradze"
print(manual_split(fullname, "a"))