from collections import deque

# Read input
f = open('input.txt', 'r')

# Vars to hold total characters processed and queue of size 4 that holds the potential marker
processed = 0
queue = deque()

# Holds signal input
signal = ""


# Read each line in the input
for line in f:
    signal = line

# Part 1
for c in signal:
    if len(queue) == 4:
        if len(queue) == len(set(queue)):
            break
        else:
            queue.popleft()
    queue.append(c)
    processed += 1

print(processed)

# Part 2
processed = 0
for c in signal:
    if len(queue) == 14:
        if len(queue) == len(set(queue)):
            break
        else:
            queue.popleft()
    queue.append(c)
    processed += 1

print(processed)