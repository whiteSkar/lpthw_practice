import random
from urllib import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = {
	"class %%%(%%%):": "Make a class named %%% that is-a %%%.",
	"class %%%(object):\n\tdef __init__(self, ***)": "class %%% has-a __init__ that take self and *** parameters.",
	"class %%%(object):\n\tdef***(self, ###)": "class %%% has-a function named ***  that takes self and @@@ parameters.",
	"*** = %%%()": "Set *** to an instance of class %%%.",
	"***.***(@@@)": "From *** get the *** function, and call it with parameters self, @@@.",
	"***.*** = '***'": "From *** get the *** atrribute and set it to '***'."
}

if len(sys.argv) == 2 and sys.argv[1] == "english":
	PHRASE_FIRST = True
else:
	PHRASE_FIRST = False

for word in urlopen(WORD_URL).readlines():
	WORDS.append(word.strip())

def convert(snippet, phrase):
	classNames = [w.capitalize() for w in random.sample(WORDS, snippet.count("%%%"))]
	otherNames = random.sample(WORDS, snippet.count('***'))
	results = []
	paramNames = []

	for i in range(0, snippet.count("@@@")):
		paramCount = random.randint(1, 3)
		paramNames.append(', '.join(random.sample(WORDS, paramCount)))
	
	for sentence in snippet, phrase:
		result = sentence[:]
		
		print result
		for word in classNames:
			result = result.replace("%%%", word, 1)
			print result

		for word in otherNames:
			result = result.replace("***", word, 1)
			print result

		for word in paramNames:
			result = result.replace("@@@", word, 1)
			print result

		results.append(result)
	print results	
	return results

try:
	while True:
		snippets = PHRASES.keys()
		random.shuffle(snippets)

		for snippet in snippets:
			phrase = PHRASES[snippet]
			question, answer = convert(snippet, phrase)
			if PHRASE_FIRST:
				question, answer = answer, question
			
			print question
			raw_input("> ")
			print "ANSWER: %s\n\n" % answer
except EOFError:
	print "\nBye"
