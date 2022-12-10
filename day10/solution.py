# Read input
f = open('input.txt', 'r')

cycle = 1 # Cycle tracker
register_val = 1 # Register value
signal_strength = 0 # Signal strength
cycle_counter = 0 # Counter to determine if an instruction has finished
inst_cycles = dict({'noop' : 1, 'addx' : 2}) # Maps cycle counter to instructions
cycles = [20, 60, 100, 140, 180, 220] # Cycles to check signal strength
register_values = [] # Captures register value for each cycle

# Read each line in the input
for line in f:
    line = line.split()
    inst = line[0]
    while True:
        # Check if we need to calculate signal strength
        if cycle in cycles:
            signal_strength += register_val * cycle

        # Start the cycle counter for the corresponding instruction
        if cycle_counter == 0:
            cycle_counter = inst_cycles[inst]

        # Update current cycle and cycle counter
        cycle += 1
        cycle_counter -= 1

        register_values.append(register_val)

        # Update register if needed
        if inst == 'addx' and cycle_counter == 0:
            val = line[1]
            register_val += int(val)

        # Move onto next instruction
        if cycle_counter == 0:
            break

print("Part 1:" + str(signal_strength))
print("---------")
print("Part 2")
row = [] 
for i in range(0, 6):
    for j in range(0, 40):
        register_val = register_values[(40 * i) + j]
        if abs(register_val - j) <= 1:
            row.append("#")
        else:
            row.append(".")
    print(*row)
    row = []
