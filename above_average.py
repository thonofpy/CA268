def above_average(lst):
	average = sum(lst)/len(lst)
	a = []
	for x in lst:
		if x > average:
			a.append(x)
	return a
