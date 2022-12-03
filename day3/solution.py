import string

# Read input
f = open('input.txt', 'r')

# Total priorities var
priorities = 0
priorities_p2 = 0

# Priority definitions
conversion = dict(((string.ascii_lowercase + string.ascii_uppercase)[i], i + 1) for i in range(len(string.ascii_lowercase + string.ascii_uppercase)))

# Group items
group_items = []

# Read each line in the input
for line in f:
    # Part 1
    c1 = line[:len(line)//2]
    c2 = line[len(line)//2:]
    item = list(set(c1) & set(c2))[0]
    priorities += conversion[item]

    # Part 2
    group_items.append(set(line.rstrip()))
    if len(group_items) == 3:
        priorities_p2 += conversion[list(set.intersection(*map(set, group_items)))[0]]
        group_items = []

# Part 1
print(priorities)

# Part 2
print(priorities_p2)