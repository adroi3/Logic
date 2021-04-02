def powerSet(currentSet):
	if (currentSet == set()):
		return {frozenset()}

	element = currentSet.pop()
	power = powerSet(currentSet)
	return power|{x|{element} for x in power}

input = {1,2,3}
resultPowerSet = powerSet(input)

print(resultPowerSet)
print(len(resultPowerSet))