def calculate_area(length, width, height):
    return (2 * length * width) + (2 * width * height) + (2 * height * length) + (length * width)


def calculate_smallest_perimeter(length, width):
    return 2 * length + 2 * width


def calculate_volume(length, width, height):
    return length * width * height


with open('input.txt', 'r') as data:
    line = data.readline().replace('\n', '')
    total_paper_area = 0
    total_ribbon_length = 0

    while line:
        dimensions = map(int, line.split('x'))
        dimensions.sort()

        length = dimensions[0]
        height = dimensions[1]
        width = dimensions[2]

        total_paper_area += calculate_area(length, height, width)

        perimeter = calculate_smallest_perimeter(length, height)
        volume = calculate_volume(length, height, width)
        total_ribbon_length += perimeter + volume

        line = data.readline().replace('\n', '')

    print 'Part 1: ', total_paper_area
    print 'Part 2: ', total_ribbon_length
