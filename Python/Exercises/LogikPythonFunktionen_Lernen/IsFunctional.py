def isRightUnique(R): 
    for (a,b) in R:
        for (c,d) in R: 
            if a==c and b!=d: 
                return False 

    return True 

def isLeftTotal(R,m): 
    return { T[0] for T in R }==m

M=set(range(1,5+1)) 

R={(1,2),(2,3) ,(3,4), (4,5) ,(5,6)}  

def isFunctional(R,m): 
    return isLeftTotal(R,m) and isRightUnique(R)

print(isFunctional(R, M))