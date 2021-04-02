def splitDice(n):
    return { (x, y) for x in range(1, n)
                       for y in range(1, n)
                           if x + y == n }
def possibleDiceRolls(n, s):  
    if n == 1:
        return { (s, ) }
    
    subPossibleDiceRolls = possibleDiceRolls(n-1,s)
    
    result = { x[:y] + z + x[y+1:]
                for x in subPossibleDiceRolls
                for y in range(len(x))
                for z in splitDice(x[y]) }

    return result

def numberDiceRolls(n, s):    
    return len(possibleDiceRolls(n, s))

print(possibleDiceRolls(2,8))
print(numberDiceRolls(2, 8))

print(numberDiceRolls(3, 9))
print(numberDiceRolls(3, 18))

print(possibleDiceRolls(3,5))
print(numberDiceRolls(3,5))
