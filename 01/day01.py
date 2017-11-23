with open('input.txt', 'r') as myfile:
    data = myfile.read().replace('\n', '')

current_floor = 0
position = 0
first_time = True

for char in data:
    position += 1
    if char == '(':
        current_floor += 1
    elif char == ')':
        current_floor -= 1

    if current_floor == -1 and first_time:
        print 'Part 2: ', position
        first_time = False

print 'Part 1: ', current_floor
