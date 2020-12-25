from collections import Counter

with open('input') as input:
	inp = [c for line in input for c in line.rstrip() ]

s = ""
c = Counter(inp)
m_c = c.most_common()[0][0]
s += inp[inp.index(m_c)]

while m_c != ";":
	immediate = [inp[i + 1] for i, x in enumerate(inp) if x == m_c]
	counts = Counter(immediate)
	s += counts.most_common()[0][0]
	m_c = counts.most_common()[0][0]

print(s)
