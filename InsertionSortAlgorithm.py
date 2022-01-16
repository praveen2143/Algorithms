def insertion_sort(array):
    for i in range(1, len(array)):
        j = i - 1
        temp = array[i]
        while j >= 0 and array[j] > temp:
            array[j + 1] = array[j]
            j = j - 1
        array[j + 1] = temp


def print_array(array):
    for i in range(len(array)):
        print(array[i], end=" ")


a = [9, 8, 7, 6, 5, 4, 3, 2,-1]
insertion_sort(a)
print_array(a)
