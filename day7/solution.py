# Read input
f = open('input.txt', 'r')

# Dictionary to hold mappings for all folders to their total sizes
dirs = {'/': 0}

# Stack to determine hierarchy of directories (last entry is the current directory)
current_dirs = ['/']

# Read each line in the input
for line in f:
    if "$ cd" in line:
        if '..' in line:
            current_dirs.pop()
        elif '/' in line:
            current_dirs = ['/']
        else:
            dst = line.split()[-1] # Directory we are going to
            if dst not in dirs:
                dst = '+'.join(current_dirs) + '+' + dst # Use unique entry name to account for duplicate directory names in other nested directories
                dirs[dst] = 0
            current_dirs.append(dst)
    elif "$" not in line:
        # Ignore the ls command and only read file sizes
        line = line.split()
        if "dir" not in line[0]:
            size = int(line[0])
            # For each nested directory we are in, update their sizes with the current file size
            for d in current_dirs:
                dirs[d] += size

# Part 1
total = 0
for v in dirs.values():
    if v <= 100000:
        total += v
print(total)

# Part 2
delete_size = 70000000
target = 30000000 - (70000000 - dirs['/'])
for v in dirs.values():
    if v <= delete_size and v >= target:
        delete_size = v
print(delete_size)
