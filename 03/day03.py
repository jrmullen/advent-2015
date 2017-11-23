with open('input.txt', 'r') as myfile:
    data = myfile.read().replace('\n', '')

visited = set()
visited_santa = set()
visited_robot = set()

x = 0
y = 0

for direction in data:
    if direction == '^':
        y += 1
    elif direction == '>':
        x += 1
    elif direction == 'v':
        y -= 1
    elif direction == '<':
        x -= 1
    visited.add((x, y))

print 'Part 1: ', len(visited)

x = 0
y = 0

f = 0
g = 0

for i in range(0, len(data), 2):
    char = data[i]
    if char == '^':
        y += 1
    elif char == '>':
        x += 1
    elif char == 'v':
        y -= 1
    elif char == '<':
        x -= 1
    visited_santa.add((x, y))

for j in range(1, len(data), 2):
    char = data[j]
    if char == '^':
        g += 1
    elif char == '>':
        f += 1
    elif char == 'v':
        g -= 1
    elif char == '<':
        f -= 1
    visited_santa.add((f, g))

print 'Part 2: ', len(visited_santa) + len(visited_robot)
