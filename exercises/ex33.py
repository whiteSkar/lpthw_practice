def printUpToNum(num):
	numbers = []

	for i in range(0, num):
		numbers.append(i)
	
	print "The numbers: "
	
	for num in numbers:
		print num

printUpToNum(int(raw_input('num? ')))

