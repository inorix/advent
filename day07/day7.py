#parse input into a dict formatted 'wire': [input]
wires = [l.strip().split() for l in open('input.txt')]
wires = {wire[-1]: wire for wire in wires}

def solve(wire):
    #argument was a number so just return that
    if wire.isdigit():
        return int(wire)
    #load actual wire data
    wire_cur = wires[wire]
    #already solved, return value
    if type(wire_cur[-1]) == int:
        return wire_cur[-1]
    #parse command and recursively solve missing input wires
    #the result is stored in the last (unused) index of the list which originally contains wire name (which we also have as the dictionary index)
    o = wire_cur[1]
    if wire_cur[0] == 'NOT':
        wires[wire][-1] = ~solve(wire_cur[1]) & 0xFFFF
    elif o == '->':
        wires[wire][-1] = solve(wire_cur[0])
    elif o == 'AND':
        wires[wire][-1] = solve(wire_cur[0]) & solve(wire_cur[2])
    elif o == 'OR':
        wires[wire][-1] = solve(wire_cur[0]) | solve(wire_cur[2])
    elif o == 'LSHIFT':
        wires[wire][-1] = solve(wire_cur[0]) << solve(wire_cur[2])
    elif o == 'RSHIFT':
        wires[wire][-1] = solve(wire_cur[0]) >> solve(wire_cur[2])
    return wires[wire][-1]
        
part1 = solve('a')        
print part1

#reset the wires, putting back wire names to last list index
for wire in wires:
    wires[wire][-1] = wire

#put first solution into b
wires['b'][-1] = part1
    
print solve('a')