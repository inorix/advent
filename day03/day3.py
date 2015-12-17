def visit(input, house = (0, 0)):
    visited = set([house])
    move = lambda (x, y), dir: {'>':(x+1, y), '<': (x-1, y), '^': (x, y-1), 'v': (x, y+1)}[dir]
    for dir in input:
        house = move(house, dir)
        visited.add(house)
    return visited

input = open('input.txt').read()

#for part 2, splitting up the input instead of dealing with two 'walkers' in the solver function results in cleaner code
print len(visit(input)), len(visit(input[::2]) | visit(input[1::2]))