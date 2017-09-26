from sys import argv

text = argv[1]

if len(text) % 2 == 0:
	print(text[len(text)//2:])
else:
	print(text[0] + text[-1])
