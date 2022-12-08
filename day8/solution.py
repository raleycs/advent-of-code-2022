def is_visible(height, i, j):
    up = True
    up_score = 0
    down = True
    down_score = 0
    left = True
    left_score = 0
    right = True
    right_score = 0

    # Check up
    row, col = i, j
    while row != 0:
        row -= 1
        coordinates = str(row) + "," + str(col)
        up_score += 1
        if height <= record[coordinates]:
            up = False
            break
    
    # Check down
    row, col = i, j
    while row != len(grid) - 1:
        row += 1
        coordinates = str(row) + "," + str(col)
        down_score += 1
        if height <= record[coordinates]:
            down = False
            break

    # Check left
    row, col = i, j
    while col != 0:
        col -= 1
        coordinates = str(row) + "," + str(col)
        left_score += 1
        if height <= record[coordinates]:
            left = False
            break
    
    # Check right
    row, col = i, j
    while col != len(grid[row]) - 1:
        col += 1
        coordinates = str(row) + "," + str(col)
        right_score += 1
        if height <= record[coordinates]:
            right = False
            break
    return (up or down or left or right), (up_score * down_score * left_score * right_score)

# Read input
f = open('input.txt', 'r')

grid = []
record = dict()
visible = 0
highest_score = -1

# Read each line in the input
for line in f:
    row = []
    for num in line:
        if num.isnumeric():
            row.append(int(num))
    grid.append(row)

for i in range(0, len(grid)):
    for j in range(0, len(grid[i])):
        coordinates = str(i) + "," + str(j)
        height = grid[i][j]
        if coordinates not in record:
            record[coordinates] = height

for i in range(0, len(grid)):
    for j in range(0, len(grid[i])):
        if (i == 0) or (i == len(grid) - 1) or (j == 0) or (j == len(grid[i]) - 1):
            visible += 1
        else:
            height = grid[i][j]
            results = is_visible(height, i, j)
            if results[0]:
                visible += 1
            if highest_score < results[1]:
                highest_score = results[1]

print('Visible: ' + str(visible))
print('Highest score: ' + str(highest_score))