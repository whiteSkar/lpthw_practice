def breakWords(stuff):
	"""This function will break up words for us."""
	return stuff.split(' ')

def sortWords(words):
	"""Sorts the words."""
	return sorted(words)

def printFirstWord(words):
	# what about this
	print words.pop(0)

def printLastWord(words):
	print words.pop(-1)

def sortSentence(sentence):
	words = breakWords(sentence)
	return sortWords(words)

def printFirstAndLast(sentence):
	words = breakWords(sentence)
	printFirstWord(words)
	printLastWord(words)

def printFirstAndLastSorted(sentence):
	words = sortSentence(sentence)
	printFirstWord(words)
	printLastWord(words)
