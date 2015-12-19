# parse input into a dict formatted 'wire': [input]
wires = [l.strip().split() for l in open('input.txt')]
wires = {wire[-1]: wire for wire in wires}

def solve(wire):
    # argument was a number so just return that
    if wire.isdigit():
        return int(wire)
    # already solved, return value
    if type(wires[wire][-1]) == int:
        return wires[wire][-1]
    # parse command and recursively solve missing input wires
    # the result is stored in the last (unused) index of the list which originally contains wire name (which we also have as the dictionary index)
    # thanks to python syntax, it's quite easy to place the result in the last index, but in many languages we are forced to calculate length
    # since the commands are not of the same length
    # parsing command to variables which will be correct most of the time
    operator = wires[wire][1]
    input1 = wires[wire][0]
    input2 = wires[wire][2]
    # exception in parsing, NOT is not in 'operator'
    if wires[wire][0] == 'NOT':
        # exception in parsing, NOT's input is not in 'input1' nor in 'input2'
        wires[wire][-1] = ~solve(wires[wire][1]) & 0xFFFF
    # -> is not even an operator! yet it is slammed in here with the operators, but hey it works right?
    elif operator == '->':
        wires[wire][-1] = solve(input1)
    elif operator == 'AND':
        wires[wire][-1] = solve(input1) & solve(input2)
    elif operator == 'OR':
        wires[wire][-1] = solve(input1) | solve(input2)
    elif operator == 'LSHIFT':
        wires[wire][-1] = solve(input1) << solve(input2)
    elif operator == 'RSHIFT':
        wires[wire][-1] = solve(input1) >> solve(input2)
    return wires[wire][-1]
        
part1 = solve('a')        
print part1

# reset the wires, putting back wire names to last list index
for wire in wires:
    wires[wire][-1] = wire

# put first solution into b
wires['b'][-1] = part1
    
print solve('a')