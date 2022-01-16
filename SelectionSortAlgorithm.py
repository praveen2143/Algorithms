def selection_sort(array):
    for i in range(len(array) - 1):
        min_index = i
        for j in range(i + 1, len(array)):
            if array[j] < array[min_index]:
                min_index = j
        array[min_index], array[i] = array[i], array[min_index]


def print_array(array):
    for i in range(len(array)):
        print(array[i], end=" ")


a = [9, 8, 7, 6, 5, 4, 3, 2,-1]
selection_sort(a)
print_array(a)
