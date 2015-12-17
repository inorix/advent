from collections import defaultdict
from itertools import permutations

people = defaultdict(dict)
names = set()

for l in open('input.txt').readlines():
    a = l.rstrip('.\r\n').split(' ')
    #names is a set, no need to check if name already there
    names.add(a[0])
    amount = int(a[3])
    if a[2] == 'lose':
        amount = -amount
    people[a[0]][a[10]] = amount

def seat():
    m = 0
    #loop over all possible seating configurations
    for seating in permutations(names):
        cur = 0
        #loop over people around the table and sum their happiness
        for person in range(0, len(seating)):
            if person < len(seating)-1 :
                cur += people[seating[person]][seating[person+1]] + people[seating[person+1]][seating[person]]
            else:
                #table is round, loop over to the start
                cur += people[seating[person]][seating[0]] + people[seating[0]][seating[person]]
        m = max(m, cur)
    return m

print seat()

#adding myself for part 2
for person in names:
    people[person]['me'] = 0
    people['me'][person] = 0
names.add('me')
    
print seat()