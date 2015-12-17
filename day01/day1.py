def move(x):
    move.floor += 1 if x == '(' else -1
    return move.floor

move.floor=0

res = map(move,open('input.txt').read())
print res[-1], res.index(-1)+1
