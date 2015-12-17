from itertools import combinations

input = sorted(map(int, list(open('input.txt'))))

#calculate minimum and maximum possible amount of containers
minlen = min([a for a in range(2, len(input)) if sum(input[:-a:-1]) >= 150])-1
maxlen = max([a for a in range(len(input)) if sum(input[:a]) <= 150])

part1 = 0
part2 = 0

#loop over amount of containers    
for a in range(minlen, maxlen):
    part2 = 0
    #check all combinations of a containers
    for b in combinations(input, a):
        if sum(b) == 150:
            part2 += 1
    #first sum will be the part 2 answer
    if not part1:
        print 'Part 2:', part2
    part1 += part2

print 'Part 1:', part1
