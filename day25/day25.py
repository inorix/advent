r = 20151125
row = 2947
col = 3029

s = sum(range(col+1))
s += sum([a+col for a in range(row-1)])

for a in range(1,s):
    r = r * 252533 % 33554393

print r
