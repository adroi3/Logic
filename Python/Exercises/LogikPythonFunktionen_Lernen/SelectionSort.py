def sort(l):
	if (len(l) == 0):
		return list()
	m = min(l)
	innerL = [x for x in l if x != m]
	return [m]+sort(innerL)

sorted = sort([5,6,1,3,9,0,2])
print(sorted)