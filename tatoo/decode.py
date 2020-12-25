import re

with open('input') as input:
	inp = [line.rstrip() for line in input]

s = ""

for line in inp:
	bits = re.findall(r'.{8}', line)
	stream = {i:int(x, 2) for i, x in enumerate(bits)}

	for i in range(32):
		if stream[i] in stream.keys():
			break
	address = stream[i]

	while stream[address] <= 39:
		address = stream[address]
	s += chr(stream[address])

print(s)
