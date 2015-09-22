from sys import argv
from os.path import exists

script, fromFile, toFile = argv

print "Copying from %s to %s" % (fromFile, toFile)

sourceData = open(fromFile).read()

print "The input file is %d bytes long" % len(sourceData)

print "Does the output file exist? %r" % exists(toFile)

open(toFile, 'w').write(sourceData)

print "Alright, all done."
