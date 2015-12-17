from itertools import combinations

input = map(int, list(open('input.txt')))

part1 = 0
part2 = 0

#loop over amount of containers    
for a in range(len(input)):
    part2 = 0
    #check all combinations of a containers
    for b in combinations(input, a):
        if sum(b) == 150:
            part2 += 1
    #first sum will be the part 2 answer
    if not part1 and part2:
        print 'Part 2:', part2
    part1 += part2

print 'Part 1:', part1
