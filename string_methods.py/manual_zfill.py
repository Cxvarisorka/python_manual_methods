def manual_zfill(string, amount, char):
    result = ''

    for i in range(amount):
        if len(result) == abs(len(string) - amount):
            break
        result += char
    
    return result + string


print(manual_zfill('luka', 8, '+'))