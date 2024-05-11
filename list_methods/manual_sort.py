def manual_sort(numbers_list, reverse=False):
    n = len(numbers_list)
    swapped = True
    
    while swapped:
        swapped = False
        for index in range(1, n):
            if (not reverse and numbers_list[index] < numbers_list[index - 1]) or (reverse and numbers_list[index] > numbers_list[index - 1]):
                temp = numbers_list[index]
                numbers_list[index] = numbers_list[index - 1]
                numbers_list[index - 1] = temp
                swapped = True
    


# Example usage
numbers = ['b', 'a', 'c']
sorted_numbers = manual_sort(numbers)
print(numbers)


numbers = list(range(10))[::-1]
print(manual_sort(numbers))