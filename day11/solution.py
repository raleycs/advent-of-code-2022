import math
from collections import deque

# Class to represent monkey and its attributes
class Monkey:
    def __init__(self, items, operation, test_val, true_send, false_send):
        self.items = items
        self.operation = operation
        self.test_val = test_val
        self.true_send = true_send
        self.false_send = false_send
        self.inspects = 0

# Read input
f = open('input.txt', 'r')

# List to hold all monkeys
monkeys = []

# Temporary monkey attributes
items, operation, test_val, true_send, false_send = [], '', -1, -1, -1

# Test vals found for each monkey
multiples = []

# Read each line in the input
for line in f:
    if 'Starting items' in line:
        line = line.replace(',', '')
        items = deque(list(map(int, line.split()[2:])))
    elif 'Operation' in line:
        line = line.replace('old', 'item')
        operation = ' '.join(line.split()[3:])
    elif 'Test' in line:
        test_val = int(line.split()[-1])
        multiples.append(test_val)
    elif 'If true' in line:
        true_send = int(line.split()[-1])
    elif 'If false' in line:
        false_send = int(line.split()[-1])
        monkeys.append(Monkey(items, operation, test_val, true_send, false_send))

# Find common multiple that can reduce size of integers while respecting mod test for each test value
common_mult = 1
for m in multiples:
    common_mult *= m

# rounds = 20 # Part 1
rounds = 10000 # Part 2
for i in range(0, rounds):
    for monkey in monkeys:
        while monkey.items:
            monkey.inspects += 1
            item = monkey.items.popleft()
            # item = math.floor(eval(monkey.operation) / 3) # Part 1
            item = eval(monkey.operation) % common_mult # Part 2
            # Test worry level
            if item % monkey.test_val == 0:
                monkeys[monkey.true_send].items.append(item)
            else:
                monkeys[monkey.false_send].items.append(item)

# Sort by number of inspects in descending order
monkeys.sort(key=lambda m: m.inspects, reverse=True)
print(monkeys[0].inspects * monkeys[1].inspects)