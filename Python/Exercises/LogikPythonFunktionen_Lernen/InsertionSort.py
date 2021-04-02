def insertion(x, L):
    if (L == list()):
        return [x]
    y = L[0]
    R = L[1:]
    if (x <= y):
        return [x]+L
    return [y]+insertion(x, R)

def insertionSort(L):
    if (L == list()):
        return list()
    
    x = L.pop()
    subInsertionSort = insertionSort(L)

    return insertion(x, subInsertionSort)

print(insertionSort([2, 1, 4, 3, 5, 10, 0]))
