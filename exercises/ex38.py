tenThings = "Apples Oranges Crows Telephoe Light Sugar"

print "Wait there ar not 10 things in that list. Let's fix that."

stuff = tenThings.split(' ')
moreStuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl",]

while len(stuff) != 10:
	next = moreStuff.pop()
	print "Adding: ", next
	stuff.append(next)
	print "There are %d items now." % len(stuff)

print "There we go: ", stuff
print "Let's do some things with stuff."

print stuff[1]
print stuff[-1]
print stuff.pop()
print ''.join(stuff)
print '#   '.join(stuff[3:5])
