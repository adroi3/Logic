def power(M):
    "Compute a list containing all subsets of the set M"
    if M == set():
        return [ set() ]
    x = M.pop()
    L = power(M)
    return L + [ K | { x } for K in L ]

def evaluate(F, I):
    'Evaluate the propositional formula F using the interpretation I'
    if isinstance(F, str):       # F is a propositional variable
        return F in I            # This variable is true iff it occurs in I
    if F[0] == '⊤': return True
    if F[0] == '⊥': return False
    if F[0] == '¬': return not evaluate(F[1], I)
    if F[0] == '∧': return evaluate(F[1], I) and evaluate(F[2], I)
    if F[0] == '∨': return evaluate(F[1], I) or evaluate(F[2], I)
    if F[0] == '→': return not evaluate(F[1], I) or evaluate(F[2], I)
    if F[0] == '↔': return evaluate(F[1], I) == evaluate(F[2], I)

def collectVars(F):
    "Collect all propositional variables occurring in the formula F"
    if isinstance(F, str):
        return { F }
    if F[0] == '⊤' or F[0] == '⊥':
        return set()
    if F[0] == '¬':
        return collectVars(F[1])
    return collectVars(F[1]) | collectVars(F[2])

def tautology(F):
    "Check, whether the formula F is a tautology"
    P = collectVars(F)
    A = power(P)
    if all(evaluate(F, I) for I in A):
        return True
    else:
        return [I for I in A if not evaluate(F, I)][0]

testFormula = ('∨', ('¬', 'a'), 'a')
print(tautology(testFormula))
