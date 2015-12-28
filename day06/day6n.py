from re import findall
import numpy as np

part1=np.zeros((1000,1000),dtype=np.bool)
part2=np.zeros((1000,1000),dtype=np.int8)

for l in open('input.txt').readlines():
    params = findall(r'(on|off|toggle|[0-9]+)', l)
    command = params.pop(0)
    x1, y1, x2, y2 = map(int, params)
    x2 += 1
    y2 += 1
    
    if command == 'on':
        part1[x1:x2, y1:y2] = 1
        part2[x1:x2, y1:y2] += 1
    if command == 'off':
        part1[x1:x2, y1:y2] = 0
        part2[x1:x2, y1:y2] -= 1
        part2[part2 < 0] = 0
    if command == 'toggle':
        part1[x1:x2, y1:y2] = np.invert(part1[x1:x2, y1:y2])
        part2[x1:x2, y1:y2] += 2

print np.sum(part1), np.sum(part2)
