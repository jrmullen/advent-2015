import re


def populate_mmatrix():
    m = []
    for x in range(1000):
        row = []
        for y in range(1000):
            row.append(0)
        m.append(row)
    return m


with open('input.txt', 'r') as myfile:
    data = myfile.read().split('\n')

instructions = []
for d in data:
    instructions.append(re.findall('\d+', d))  # Extract only the numbers into a list

instructions = [map(int, i) for i in instructions]  # Convert string to int

matrix = populate_mmatrix()
part_2 = populate_mmatrix()

for i in range(len(data)):
    if data[i].startswith('turn on '):
        for j in range(instructions[i][0], instructions[i][2] + 1):
            for k in range(instructions[i][1], instructions[i][3] + 1):
                matrix[k][j] = 1
                part_2[k][j] += 1

    if data[i].startswith('toggle '):
        for j in range(instructions[i][0], instructions[i][2] + 1):
            for k in range(instructions[i][1], instructions[i][3] + 1):
                if matrix[k][j] == 1:
                    matrix[k][j] = 0
                elif matrix[k][j] == 0:
                    matrix[k][j] = 1
                part_2[k][j] += 2

    if data[i].startswith('turn off '):
        for j in range(instructions[i][0], instructions[i][2] + 1):
            for k in range(instructions[i][1], instructions[i][3] + 1):
                matrix[k][j] = 0
                if part_2[k][j] > 0:
                    part_2[k][j] -= 1

print 'Part 1: ', sum(x.count(1) for x in matrix)
print 'Part 2: ', sum([sum(p) for p in part_2])
