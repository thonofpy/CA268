from sys import argv

text = argv[1:]

if len(text) != 0:
	print(":" + ":".join(text) + ":")
