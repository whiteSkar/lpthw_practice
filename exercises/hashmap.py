def new(num_buckets = 256):
	aMap = []
	for i in range(0, num_buckets):
		aMap.append([])
	return aMap

def hashKey(aMap, key):
	return hash(key) % len(aMap)

def getBucket(aMap, key):
	bucketId = hashKey(aMap, key)
	return aMap[bucketId]

def getSlot(aMap, key, defaultValue = None):
	bucket = getBucket(aMap, key)

	for i, kv in enumerate(bucket):
		k, v = kv
		if key == k:
			return i, k, v
	return -1, key, defaultValue

def get(aMap, key, defaultValue = None):
	i, k, v = getSlot(aMap, key, defaultValue = defaultValue)
	return v

def set(aMap, key, value):
	bucket = getBucket(aMap, key)
	i, k, v = getSlot(aMap, key)

	if i >= 0:
		bucket[i] = (key, value)
	else:
		bucket.append((key, value))
	
def delete(aMap, key):
	bucket = getBucket(aMap, key)

	for i in xrange(len(bucket)):
		k, v = bucket[i]
		if key == k:
			del bucket[i]
			break;

def list(aMap):
	for bucket in aMap:
		if bucket:
			for k, v in bucket:
				print k, v
