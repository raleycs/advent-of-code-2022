# Read input
f = open('input.txt', 'r')

visited = dict({"0,0" : True})
visited_once = 1

row_head, col_head = 0, 0
row_tail, col_tail = 0, 0

# Read each line in the input
for line in f:
    line = line.split()
    direction = line[0]
    moves = line[1]

    for i in range(0, int(moves)):
        if direction == "R":
            col_head += 1
            if abs(col_head - col_tail) > 1:
                if abs(row_head - row_tail) != 0:
                    row_tail = row_head
                col_tail += 1
        elif direction == "L":
            col_head -= 1
            if abs(col_head - col_tail) > 1:
                if abs(row_head - row_tail) != 0:
                    row_tail = row_head
                col_tail -= 1
        elif direction == "U":
            row_head += 1
            if abs(row_head - row_tail) > 1:
                if abs(col_head - col_tail) != 0:
                    col_tail = col_head
                row_tail += 1
        else:
            row_head -= 1
            if abs(row_head - row_tail) > 1:
                if abs(col_head - col_tail) != 0:
                    col_tail = col_head
                row_tail -= 1
        current_tail = ",".join([str(col_tail), str(row_tail)])
        current_head = ",".join([str(col_head), str(row_head)])
        if current_tail not in visited:
            visited[current_tail] = True
            visited_once += 1
        # print("Head: " + current_head)
        # print("Tail: " + current_tail)
        # print("---------")

# for location, been_visited in visited.items():
#     if been_visited:
        # print(location)
print(visited_once)