import re
from collections import defaultdict

positions = defaultdict(int)

dirs 	= {"U":(0,-1), "D":(0,1), "L":(-1, 0), "R":(1,0)}

visited = []
starts	= []
ends 	= []
walls 	= []


def visualizer():
	i = -20
	while (i < 155):
		j = -10
		while (j < 140):
			if ((j, i) in starts):
				print('S', end = '')
			elif ((j, i) in ends):
				print('F', end = '')
			elif ((j, i) in walls):
				print('#', end = '')
			elif (positions[(j, i)] == 1):
				print('V', end = '')
			else:
				print('.', end = '')
			j += 1
		print('')
		i += 1


def find(path, route):

	while True:
		location = path[0]

		for Key in dirs:
			Value = dirs[Key]
			new_pos = tuple([location[0] + Value[0], location[1] + Value[1]])

			if	new_pos in positions and new_pos not in visited:
				if positions[new_pos] == 2:
					route.append((new_pos, path[1] + Key))
					return route[-1]

				if positions[new_pos] != -1:
					route.append((new_pos, path[1] + Key))
					visited.append(new_pos)

		route = route[1:]

		if len(route) == 0:
			return route
		path = route[0]



with open('input') as input:
	inp = [line.rstrip() for line in input]

for line in inp:
	s = re.findall(r'\d+', line)
	start = [int(s[0]), int(s[1])]
	positions[tuple(start)] = 0

	if " " in line:
		line = line[line.index(' ') + 1:]
		for x in line.split(','):
			if (x == 'F'):
				ends.append(tuple(start))
				positions[tuple(start)] = 2
			elif (x == 'S'):
				starts.append(tuple(start))
				positions[tuple(start)] = 0
			elif (x == 'X'):
				walls.append(tuple(start))
				positions[tuple(start)] = -1
			else :
				start[0] += dirs[x][0]
				start[1] += dirs[x][1]
				positions[tuple(start)] = 1


for coords in starts:
	print(find((coords, ""), []))

# Because positions is a defaultdict, running the visuzalizer below will add keys to the dictionary and therefore invalidate the ouput.
# For this reason it is better to run it after the path finding finished

visualizer()
