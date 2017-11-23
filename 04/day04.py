import hashlib

with open('input.txt', 'r') as myfile:
    data = myfile.read().replace('\n', '')

count = 0
value = data + repr(count)
part1 = True

while True:
    if hashlib.md5(value).hexdigest().startswith('00000') and part1:
        print 'Part 1: ', count
        part1 = False
    elif hashlib.md5(value).hexdigest().startswith('000000'):
        print 'Part 2: ', count
        break
    else:
        count += 1
        value = data + repr(count)
