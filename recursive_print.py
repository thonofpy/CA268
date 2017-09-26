def rprint(a, b):
	if a == b:
		pass
	else:
		print(a)
		rprint(a + 1, b)
