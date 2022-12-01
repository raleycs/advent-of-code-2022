import heapq

# Read input
f = open('input.txt', 'r')

# Max calories var
max_calories = -1
current_calories = 0

# list to convert to min-max heap
calories = []

# Read each line in the input
for line in f:
    if line == "\n":
        if current_calories > max_calories:
            max_calories = current_calories
        calories.append(current_calories) 
        current_calories = 0
        continue
    current_calories += int(line)

# Part 1 solution
# Time-complexity: O(n)
print(max_calories)

# Part 2 solution
# Time-complexity: O(n log(n))
heapq.heapify(calories)
top_3 = heapq.nlargest(3, calories)
print(sum(top_3))