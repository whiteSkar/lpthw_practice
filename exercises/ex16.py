from sys import argv

script, fileName = argv

print "We're going to earse %r." %fileName
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(fileName, 'w')

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

output = "%s\n%s\n%s\n" % (line1, line2, line3)
target.write(output)

print "And finally, we close it."
target.close()