with open('input.txt', 'r') as myfile:
    data = myfile.read().split()

nice_count_p1 = 0
nice_count_p2 = 0
not_allowed = ('ab', 'cd', 'pq', 'xy')

for string in data:
    num_vowels = 0
    double_char = False
    three_vowels = False
    nice_string = False
    previous_char = ''

    for char in string:
        if char in 'aeoiu':
            num_vowels += 1
        if previous_char == char:
            double_char = True
        previous_char = char

    if num_vowels >= 3:
        three_vowels = True

    if double_char and three_vowels:
        nice_string = True

    for x in not_allowed:
        if x in string:
            nice_string = False

    if nice_string:
        nice_count_p1 += 1

print 'Part 1: ', nice_count_p1

# Part 2
def has_disjoint_pair(s):
    i = 1
    while i < len(s):
        xy = s[i - 1] + s[i]
        if xy in s[i + 1:]:
            return True
        i += 1
    return False


def has_xyx(s):
    i = 2
    while i < len(s):
        if s[i - 2] == s[i]:
            return True
        i += 1
    return False


for string in data:
    if has_disjoint_pair(string) and has_xyx(string):
        nice_count_p2 += 1

print 'Part 2: ', nice_count_p2
