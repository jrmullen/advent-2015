with open('input.txt', 'r') as myfile:
    data = myfile.read().replace('\n', '')

current_floor = 0
position = 0

for char in data:
    position += 1
    if char == '(':
        current_floor += 1
    elif char == ')':
        current_floor -= 1

    if current_floor == -1:
        print position
        break

print(current_floor)
