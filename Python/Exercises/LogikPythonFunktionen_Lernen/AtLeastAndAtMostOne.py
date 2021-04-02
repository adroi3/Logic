def atLeastOne(M):
    return { frozenset(M) }
    
def atMostOne(V):
    return { frozenset({ ('¬', p), ('¬', q) })
            for p in V
            for q in V
                if p != q }

M = { "a","b","c" }
print(atLeastOne(M))
print(atMostOne(M))
