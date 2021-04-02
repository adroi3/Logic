def permutationHelper(n, originalN):
    if n == 1:
        return { (x, ) for x in range(1, originalN+1) }
    
    subAllPermutations = permutationHelper(n-1, originalN)
    
    return { y + (x,) for x in range(1, originalN+1)
                       for y in subAllPermutations
                           if x not in y }

def allPermutations(n):
    'This function returns the set of all permutations of length n.'
    return permutationHelper(n, n)
    
    

print(allPermutations(3))
