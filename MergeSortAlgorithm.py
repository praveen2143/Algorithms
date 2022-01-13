def mergesort(array):
    if len(array) > 1:
        m = len(array) // 2
        L = array[:m]
        R = array[m:]

        mergesort(L)
        mergesort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            array[k] = R[j]
            j += 1
            k += 1

def printlist(array):
    #print()
    for i in range(len(array)):
        print(array[i], end=" ")


if __name__ == '__main__':
    a = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    mergesort(a)
    printlist(a)
