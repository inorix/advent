from re import findall

part1=0
part2=0

for l in open('input.txt').readlines():
    #sorting the parsed input takes care of most challenges in this puzzle
    a = sorted(map(int,findall('[0-9]+',l)))
    part1 += a[0]*a[1]*3+a[0]*a[2]*2+a[1]*a[2]*2
    part2 += (a[0]+a[1])*2+a[0]*a[1]*a[2]
    
print part1,part2