def binary_search(list, item):
    low = 0
    height = len(list) - 1

    while low <= height:
        mid = (low + height)
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            height = mid - 1
        else:
            low = mid + 1
    return None


my_list = [1, 3, 5, 7, 9]

print(binary_search(my_list, 3))
print(binary_search(my_list, -1))
