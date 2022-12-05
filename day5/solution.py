import re

# Read input
f = open('input.txt', 'r')

# Part 1

# Var to hold all stacks of crates
stacks = []

# Bool to determine when to read procedures
read_procedures = False

# Read each line in the input
for line in f:
    if line == "\n":
        read_procedures = True
        continue
    # Begin shifting crates
    if read_procedures:
        line = line.split()
        num_crates = int(line[1])
        src_crate = int(line[3]) - 1
        dst_crate = int(line[-1]) - 1

        # While there are crates to move, pop from the source crate and move to the destination crate
        while num_crates != 0:
            stacks[dst_crate].append(stacks[src_crate].pop())
            num_crates -= 1
    else:
        # Parse the input into the appropriate stacks
        for i in range(0, len(line)):
            if line[i].isalpha():
                # Append stacks of crates (empty) if not already created
                if not stacks:
                    stacks_to_add = len(line) // 4
                    while stacks_to_add != 0:
                        stacks.append([])
                        stacks_to_add -= 1
                stacks[i // 4].insert(0, line[i])

print(''.join(list(map(lambda x: x[-1], stacks))))

# Part 2

# Reset variables
stacks = []
read_procedures = False

# Reset file pointer
f.seek(0)

# Read each line in the input
for line in f:
    if line == "\n":
        read_procedures = True
        continue
    # Begin shifting crates
    if read_procedures:
        line = line.split()
        num_crates = int(line[1])
        src_crate = int(line[3]) - 1
        dst_crate = int(line[-1]) - 1

        # Use list indexing to copy over crates from source to destination
        crates_to_move = stacks[src_crate][(
            len(stacks[src_crate]) - num_crates):]
        for c in crates_to_move:
            stacks[dst_crate].append(c)

        # Pop the elements that were copied to the destination stack since they are now moved
        while num_crates != 0:
            stacks[src_crate].pop()
            num_crates -= 1
    else:
        # Parse the input into the appropriate stacks
        for i in range(0, len(line)):
            if line[i].isalpha():
                # Append stacks of crates (empty) if not already created
                if not stacks:
                    stacks_to_add = len(line) // 4
                    while stacks_to_add != 0:
                        stacks.append([])
                        stacks_to_add -= 1
                stacks[i // 4].insert(0, line[i])

print(''.join(list(map(lambda x: x[-1], stacks))))