def solve(part):
    grid = []

    for l in open('input.txt'):
        grid.append([1 if c == '#' else 0 for c in l])
        
    maxlen = len(l)

    if part == 2:
        grid[0][0] = 1
        grid[maxlen-1][0] = 1
        grid[0][maxlen-1] = 1
        grid[maxlen-1][maxlen-1] = 1
        
    for b in range(100):
        change = []
        for y in range(maxlen):
            for x in range(maxlen):
                s = 0
                #check neighbors if they are inside the grid
                for n in [[-1,-1],[0,-1],[1,-1],[-1,0],[1,0],[-1,1],[0,1],[1,1]]:
                    if x+n[0] >= 0 and x+n[0] < maxlen and y+n[1] >= 0 and y+n[1] < maxlen:
                        if grid[x+n[0]][y+n[1]] == 1:
                            s += 1
                #changes are stored until we finish checking everything
                if grid[x][y] == 1 and s < 2 or s > 3:
                    #skip corners for part 2
                    if part == 1 or [x, y] not in [[0, 0], [maxlen-1, 0], [0, maxlen-1], [maxlen-1, maxlen-1]]:
                        change.append([x, y, 0])
                if grid[x][y] == 0 and s == 3:
                    change.append([x, y, 1])
        #apply changes
        for c in change:
            grid[c[0]][c[1]] = c[2]
            
    return sum(sum(grid, []))

print solve(1)
print solve(2)