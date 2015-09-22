def cheeseAndCrackers(cheeseCount, boxesOfCrackers):
	print "You have %d cheeses!" % cheeseCount
	print "You have %d boxes of crackers!" % boxesOfCrackers
	print "Man that's enough for a party!"
	print "Get a blanket.\n"
	print 1
	print "%d" % amountOfCheese

print "We can just give the function numbers directly:"
cheeseAndCrackers(20, 30)

print "OR, we can use variables from our scripts:"
amountOfCheese = 10
amountOfCrackers = 50

cheeseAndCrackers(amountOfCheese, amountOfCrackers)

print "We can even do math inside too:"
cheeseAndCrackers(10 + 20, 5 + 6)

print "And we can combine the two, variables and math:"
cheeseAndCrackers(amountOfCheese + 100, amountOfCrackers + 1000)

