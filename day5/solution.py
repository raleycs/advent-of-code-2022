# Read input
f = open('input.txt', 'r')

# Part 1

# Var to hold all stacks of crates
stacks = []
stacks_p2 = []

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

        # Use list indexing to copy over crates from source to destination
        crates_to_move = stacks_p2[src_crate][(
            len(stacks_p2[src_crate]) - num_crates):]
        for c in crates_to_move:
            stacks_p2[dst_crate].append(c)

        # While there are crates to move, pop from the source crate and move to the destination crate
        while num_crates != 0:
            stacks[dst_crate].append(stacks[src_crate].pop())
            stacks_p2[src_crate].pop()
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
                        stacks_p2.append([])
                        stacks_to_add -= 1
                
                # Add current crate to stacks
                stacks[i // 4].insert(0, line[i])
                stacks_p2[i // 4].insert(0, line[i])

# Part 1
print(''.join(list(map(lambda x: x[-1], stacks))))

# Part 2
print(''.join(list(map(lambda x: x[-1], stacks_p2))))