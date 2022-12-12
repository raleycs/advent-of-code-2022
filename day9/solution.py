import numpy as np

class Knot:
    def __init__(self, id: int, x: int, y: int):
        self.id = id # Debugging
        self.x = x
        self.y = y
    def __sub__(self, knot):
        return Knot(-1, self.x - knot.x, self.y - knot.y)
    def norm(self):
        return np.linalg.norm([self.x, self.y])

rope_moves = [direction_steps.split() for direction_steps in open('input.txt')]

# total_knots = 2 # Part 1
total_knots = 10 # Part 2
rope = [Knot(n, 0, 0) for n in range(total_knots)]
tail_positions = {(rope[-1].x, rope[-1].y)}

for direction, magnitude in rope_moves:
    for _ in range(int(magnitude)):
        if direction == 'U':
            rope[0].y += 1
        elif direction == 'D':
            rope[0].y -= 1
        elif direction == 'R':
            rope[0].x += 1
        else:
            rope[0].x -= 1
        for i in range(total_knots - 1):
            # If distance is greater than 2, adjust
            if (rope[i] - rope[i + 1]).norm() >= 2:
                rope[i + 1].x += (rope[i + 1].x != rope[i].x) * np.sign(rope[i].x - rope[i + 1].x)
                rope[i + 1].y += (rope[i + 1].y != rope[i].y) * np.sign(rope[i].y - rope[i + 1].y)
                if i + 1 == total_knots - 1:
                    tail_positions.add((rope[total_knots - 1].x, rope[total_knots - 1].y))

print(len(tail_positions))
