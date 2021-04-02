def toDigitsOther(digits):
    digitsAsString = str(digits)

    return [ int(c) for c in digitsAsString ]

def toDigitsMod(digits):
    if digits == 0:
        return []

    digit = digits % 10
    newDigits = digits // 10

    return toDigitsMod(newDigits) + [digit]

def relationalProduct(R1, R2):
    return { (x, z) for (x, y1) in R1 for (y2, z) in R2 if y1 == y2 }

def transitiveClosure(R):
    T = R

    while True:
        oldT = T

        T = relationalProduct(R, T) | R

        if oldT == T:
            return T

def subset(M, n):
    if n == 0:
        return {frozenset()}
    return { rec | {m} for m in M for rec in subset(M, n-1) if m not in rec }

def powerSet(M):
    if M == set():
        return {frozenset()}
    clonedSet = set(M)
    
    element = clonedSet.pop()
    recPowerSet = powerSet(clonedSet)

    return recPowerSet | { m | {element} for m in recPowerSet }

def subList(L):
    if L == list():
        return [[]]
    
    elem = L[0]
    newL = L[1:]

    subL = subList(newL)

    return subL + [ [elem] + l for l in subL ]

def selectionSort(L):
    if L == list():
        return L
    
    mini = min(L)
    newL = [ e for e in L if e != mini ]

    subSelectionSort = selectionSort(newL)

    return [mini] + subSelectionSort

def powerSetWithLists(M):
    if M == set():
        return [set()]
    
    clonedM = set(M)
    element = clonedM.pop()

    subPower = powerSetWithLists(clonedM)

    return subPower + [ {element} | m for m in subPower ]

def insertIntoSortedList(L, x):
    for i in range(len(L)):
        if x <= L[i]:
            return L[:i] + [x] + L[i:]
    return L + [x]

def insertionSort(L):
    if len(L) == 0:
        return []

    clonedL = list(L)
    x = clonedL.pop()

    subInsertionSort = insertionSort(clonedL)

    return insertIntoSortedList(subInsertionSort, x)


print(insertionSort([2,1, 0, 3, 4]))