import sys

name = sys.argv[1]

i = 0
j = 1
while i < len(name):
	if i == len(name) or j == len(name):
		sys.exit()
	print(name[i] + name[j])
	i = i + 1
	j = j + 1
