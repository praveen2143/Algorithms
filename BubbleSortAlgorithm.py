def bubble_sort(array):
    for i in range(len(array)):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]


def print_array(array):
    for i in range(len(array)):
        print(array[i],end=" ")


a = [9,8,7,6,5,4,3,2,1]
bubble_sort(a)
print_array(a)
