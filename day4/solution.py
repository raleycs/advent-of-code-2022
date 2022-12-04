import string

# Read input
f = open('input.txt', 'r')

# Total overlaps var
overlaps = 0

# Total range overlaps var
range_overlaps = 0

# List containing all sections within ranges
ranges = []

# Read each line in the input
for line in f:
    if line == "\n":
        continue
    line = line.split(',')
    p1_x = int(line[0].split('-')[0])
    p1_y = int(line[0].split('-')[1])
    p2_x = int(line[1].split('-')[0])
    p2_y = int(line[1].split('-')[1])

    p1 = range(p1_x, p1_y)
    p2 = range(p2_x, p2_y)

    # Check local bounds
    if p1_x >= p2_x and p1_y <= p2_y:
        overlaps += 1
    elif p2_x >= p1_x and p2_y <= p1_y:
        overlaps += 1

    # Part 2 get ranges
    if p1_x <= p2_y and p2_x <= p1_y:
        ranges.append(range(max(p1.start, p2.start), min(p1.stop, p2.stop)))

# Part 1
print(overlaps)

# Part 2
print(len(ranges))
