def subSet(currentSet, amount):
	if amount == 0:
		return {frozenset()}
	return { y|{x}
				for x in currentSet
				for y in subSet(currentSet, amount-1)
					if x not in y }

print(subSet({1,2,3},2))