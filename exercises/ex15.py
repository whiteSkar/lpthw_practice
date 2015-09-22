from sys import argv

script, fileName = argv

file = open(fileName)

print "Here's your file %r:" % fileName
print file.read()

file.close()
