import hashmap

states = hashmap.new()
hashmap.set(states, 'Oregon', 'OR')
hashmap.set(states, 'Florida', 'FL')
hashmap.set(states, 'California', 'CA')
hashmap.set(states, 'New York', 'NY')
hashmap.set(states, 'Michigan', 'MI')

cities = hashmap.new()
hashmap.set(cities, 'CA', 'San Francisco')
hashmap.set(cities, 'MI', 'Detroit')
hashmap.set(cities, 'FL', 'Jacksonville')
hashmap.set(cities, 'NY', 'New York')
hashmap.set(cities, 'OR', 'Portland')

print '-' * 10
print "NY state has: ", hashmap.get(cities, 'NY')
print "OR state has: ", hashmap.get(cities, 'OR')

print '-' * 10
print "Michigan's abbreviation is: ", hashmap.get(states, 'Michigan')
print "Florida's abbreviation is: ", hashmap.get(states, 'Florida')

print '-' * 10
print "Michigan has: ", hashmap.get(cities, hashmap.get(states, 'Michigan'))
print "Florida has: ", hashmap.get(cities, hashmap.get(states, 'Florida'))

print '-' * 10
hashmap.list(states)

print '-' * 10
hashmap.list(cities)

print '-' * 10
state = hashmap.get(states, 'Texas')

if not state:
	print "Sorry, no Texas. %r" % state

city = hashmap.get(cities, 'TX', 'Does Not Exist')
print "The city for the state 'TX' is: %s" % city
