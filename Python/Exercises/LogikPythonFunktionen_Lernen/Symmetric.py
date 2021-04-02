def isSymmetric(R):
    return all( (y,x) in R for (x,y) in R  )

R = { (1, 2), (2, 1) }#, (3, 1) }

print(isSymmetric(R))