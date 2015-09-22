from sys import argv

script, input_file = argv

def printAll(f):
	print f.read()

def rewind(f):
	f.seek(0)

def printALine(lineCount, f):
	print lineCount, f.readline(),

currentFile = open(input_file)

print "First let's print the whole file:\n"

printAll(currentFile)

print "Now let's rewind, kind of like a tape."

rewind(currentFile)

print "Let's print three lines:"

currentLine = 1
printALine(currentLine, currentFile)

currentLine = currentLine + 1
printALine(currentLine, currentFile)

currentLine += 1
printALine(currentLine, currentFile)

currentFile.close()
