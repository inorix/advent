from re import findall

part1=[[0]*1000 for i in range(1000)]
part2=[[0]*1000 for i in range(1000)]

for l in open('input.txt').readlines():
    coords = findall(r'(on|off|toggle|[0-9]+)', l)
    command = coords.pop(0)
    coords = map(int, coords)

    #the two lambdas return the new value for the light
    exec1 = lambda x, y: {'on': 1, 'off': 0, 'toggle': not x}[y]
    exec2 = lambda x, y: {'on': x+1, 'off': max(x-1, 0), 'toggle': x+2}[y]   
    
    for x in range(coords[0],coords[2]+1):
        for y in range(coords[1],coords[3]+1):
            part1[x][y] = exec1(part1[x][y], command)
            part2[x][y] = exec2(part2[x][y], command)

#flattening the nested list to get the results
print sum(sum(part1, []))
print sum(sum(part2, []))
