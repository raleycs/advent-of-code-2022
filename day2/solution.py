# Read input
f = open('input.txt', 'r')

# Total score var
score = 0
score_p2 = 0

# Mapping moves to point values
moves = dict()
moves['X'] = 1
moves['Y'] = 2
moves['Z'] = 3

# Mapping outcomes to point values
outcomes = dict()
outcomes['draw'] = 3
outcomes['win'] = 6

# Read each line in the input
for line in f:
    line = line.split()
    if len(line) == 2:
        opponent = line[0]
        yours = line[1]

        # Calculate scores
        score += moves[yours]
        if opponent == "A":
            if yours == "X":
                score += outcomes['draw']
                score_p2 += moves['Z']
            elif yours == "Y":
                score += outcomes['win']
                score_p2 += moves['X'] + outcomes['draw']
            elif yours == "Z":
                score_p2 += moves['Y'] + outcomes['win']
        elif opponent == "B":
            if yours == "X":
                score_p2 += moves['X']
            elif yours == "Y":
                score += outcomes['draw']
                score_p2 += moves['Y'] + outcomes['draw']
            elif yours == "Z":
                score += outcomes['win']
                score_p2 += moves['Z'] + outcomes['win']
        elif opponent == "C":
            if yours == "X":
                score += outcomes['win']
                score_p2 += moves['Y']
            elif yours == "Y":
                score_p2 += moves['Z'] + outcomes['draw']
            elif yours == "Z":
                score += outcomes['draw']
                score_p2 += moves['X'] + outcomes['win']

# Part 1 solution
# Time-complexity: O(n)
print(score)

# Part 2 solution
# Time-complexity: O(n)
print(score_p2)
