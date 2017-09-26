def get_plural(word):

	es = ("ch", "sh", "x", "s", "z", "o")
	vowel = ("a", "e", "i", "o", "u")
	ves = ("f", "fe")

	if word[-2:] in es or word[-1] in es:
		return word + "es"
	elif word[-1] == "y" and word[-2] not in vowel:
		return word[:-1] + "ies"
	elif word[-1] == "f":
		return word[:-1] + "ves"
	elif word[-2:] == "fe":
		return word[:-2] + "ves"
	else:
		return word + "s"
