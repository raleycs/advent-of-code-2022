import gmpy2
import math
from collections import deque
from gmpy2 import mpz

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
f = open('sample.txt', 'r')

# List to hold all monkeys
monkeys = []

# Temporary monkey attributes
items, operation, test_val, true_send, false_send = [], '', -1, -1, -1

# Read each line in the input
for line in f:
    if 'Starting items' in line:
        line = line.replace(',', '')
        items = deque(list(map(int, line.split()[2:])))
    elif 'Operation' in line:
        # line = line.replace('old', 'item')
        line = line.replace('old', 'a')
        operation = ' '.join(line.split()[3:])
    elif 'Test' in line:
        test_val = int(line.split()[-1])
    elif 'If true' in line:
        true_send = int(line.split()[-1])
    elif 'If false' in line:
        false_send = int(line.split()[-1])
        monkeys.append(Monkey(items, operation, test_val, true_send, false_send))

# Part 1
for i in range(0, 20):
    for monkey in monkeys:
        while monkey.items:
            monkey.inspects += 1
            item = mpz(monkey.items.popleft())
            item = math.floor(eval(monkey.operation) / 3)
            # Test worry level
            if item % monkey.test_val == 0:
                monkeys[monkey.true_send].items.append(item)
            else:
                monkeys[monkey.false_send].items.append(item)

# Sort by number of inspects in descending order
monkeys.sort(key=lambda m: m.inspects, reverse=True)

print(monkeys[0].inspects * monkeys[1].inspects)

# Part 2
# for i in range(0, 20):
#     for monkey in monkeys:
#         monkey.inspects += monkey.items.size
#         a = monkey.items
#         monkey.items = np.array(np.floor(ne.evaluate("(" + monkey.operation + ") / 3")), dtype=object)
#         # monkey.items = np.array(ne.evaluate(monkey.operation), dtype=object)
#         true_append = monkey.items[monkey.items % monkey.test_val == 0]
#         monkeys[monkey.true_send].items = np.array(np.append(monkeys[monkey.true_send].items, true_append), dtype=object)
#         false_append = monkey.items[monkey.items % monkey.test_val != 0]
#         monkeys[monkey.false_send].items = np.array(np.append(monkeys[monkey.false_send].items, false_append), dtype=object)
#         monkey.items = np.array([])

    # print(f"After round {i + 1}, the monkeys are holding items with these worry levels:")
    # for m in range(0, len(monkeys)):
    #     it = ''.join(str(monkeys[m].items.tolist()))
    #     print(f'Monkey {m}: {it}')
    #     print(f'Monkey {m} inspected items {monkeys[m].inspects} times and has {len(monkeys[m].items)} items.')
    # print('------------------')
    # if i == 2:
    #     exit()

# Sort by number of inspects in descending order
# monkeys.sort(key=lambda m: m.inspects, reverse=True)

# for monkey in monkeys:
#     print(monkey.inspects)

# print(monkeys[0].inspects * monkeys[1].inspects)
