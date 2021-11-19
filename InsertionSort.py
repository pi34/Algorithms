def insertionSort (A):

    for i in range(1, len(A)):
        val = A[i]
        j = i - 1
        while (j >= 0) and (A[j] > val):
            A[j+1] = A[j]
            j = j - 1
        A[j+1] = val

    return print(A)
