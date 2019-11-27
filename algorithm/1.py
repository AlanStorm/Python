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


# print(binary_search(my_list, 3))
# print(binary_search(my_list, -1))


def find_smallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selection_sort(arr):
    new_arr = []
    for i in range(len(arr)):
        smallest = find_smallest(arr)
        new_arr.append(arr.pop(smallest))
    return new_arr


# print(selection_sort([5, 3, 6, 2, 10]))


def greet(name):
    print("hello, " + name + "!")
    greet2(name)
    print("getting ready to say bye...")
    bye()


def greet2(name):
    print("how are you," + name + "?")


def bye():
    print('ok bye')


# greet('maggie')

def sum(arr):
    total = 0
    for x in arr:
        total += x
    return total


# print(sum([1, 2, 3, 4]))

