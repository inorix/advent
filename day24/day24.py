from itertools import combinations
from operator import mul

a = map(int, [l.strip() for l in open('input.txt')])

part1, part2 = 1e30, 1e30

for b in range(2, len(a) / 3):
    for c in combinations(a, b):
        if sum(c) == sum(a) / 3:
            part1 = min(part1, reduce(mul, c))
        elif sum(c) == sum(a) / 4:
            part2 = min(part2, reduce(mul, c))
        if part1 < 1e30 and part2 < 1e30:
            print part1, part2
            quit()