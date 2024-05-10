def manual_title(string):
    words = string.split(" ")
    result = []
    for word in words:
        result.append(word.capitalize())
    return " ".join(result)


print(manual_title('luka gamarjoba 2nd var'))