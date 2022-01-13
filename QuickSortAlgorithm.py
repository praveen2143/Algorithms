def partition(array, start, end):
    # num = array[len(array) - 1]
    i = j = start
    while j in range(start, end):
        if array[j] < array[end]:
            array[i], array[j] = array[j], array[i]
            i += 1
        j += 1

    array[i], array[end] = array[end], array[i]
    return i


def quicksort(array, start, end):
    if start < end:
        pos = partition(array, start, end)
        quicksort(array, start, pos - 1)
        quicksort(array, pos + 1, end)


def printlist(array):
    # print()
    for i in range(len(array)):
        print(array[i], end=" ")


if __name__ == '__main__':
    a = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    quicksort(a, 0, len(a) - 1)
    printlist(a)
