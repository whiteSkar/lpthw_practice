def secretFormula(started):
	jellyBeans = started * 500
	jars = jellyBeans / 1000
	crates = jars / 100
	return jellyBeans, jars, crates

startPoint = 10000
beans, jars, crates = secretFormula(startPoint)

print "Starting Point: %d" % startPoint
print "We have %d beans, %d jars, and %d crates." % (beans, jars, crates)

startPoint /= 10

print "another with 10 times less startPoint."
print "We have %d beans, %d jars, and %d crates." % (secretFormula(startPoint))
