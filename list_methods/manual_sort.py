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
numbers = [38, 27, 43, 3, 9, 82, 10]
sorted_numbers = manual_sort(numbers, reverse=True)
print(sorted_numbers)


numbers = list(range(10))[::-1]
print(manual_sort(numbers))