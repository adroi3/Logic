def allSublists(L):
    if len(L)==0:
        return [[]]

    x = L.pop(0)

    P1=allSublists(L)

    return [[x]+A for A in P1] + P1

print(allSublists([1,3,2]))
print(len(allSublists([1,3,2])))