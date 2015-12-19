# parse input into a dict formatted 'wire': [reversed input]
wires = [l.strip().split() for l in open('input.txt')]
wires = {wire[-1]: wire[::-1] for wire in wires}

def solve(wire):
    # argument was a number so just return that
    if wire.isdigit():
        return int(wire)
    # already solved, return value
    if type(wires[wire][0]) == int:
        return wires[wire][0]
    # parse command and recursively solve missing input wires
    # the result is stored in the first (unused) index of the list which originally contains wire name (which we also have as the dictionary index)
    # this version stores result in the first index, no need for any length checks
    # a bit strange to call first input wire 'input2' but i wanted the code to be as similar as possible to the other version
    # index 0 is always the destination wire and index 1 is always '->', no need to bother parsing those
    input2 = wires[wire][2]
    # if there's more input, we expect an operator coming
    if len(wires[wire]) > 3:
        operator = wires[wire][3]
    # if there's more input, we expect another input wire coming
    if len(wires[wire]) > 4:
        input1 = wires[wire][4]
    # if there is no operator, this is an assignment
    if 'operator' not in vars():
        wires[wire][0] = solve(input2)
    # NOT is in 'operator' and its input is in 'input2', all neat!
    elif operator == 'NOT':
        wires[wire][0] = ~solve(input2) & 0xFFFF
    elif operator == 'AND':
        wires[wire][0] = solve(input1) & solve(input2)
    elif operator == 'OR':
        wires[wire][0] = solve(input1) | solve(input2)
    elif operator == 'LSHIFT':
        wires[wire][0] = solve(input1) << solve(input2)
    elif operator == 'RSHIFT':
        wires[wire][0] = solve(input1) >> solve(input2)
    return wires[wire][0]
        
part1 = solve('a')        
print part1

# reset the wires, putting back wire names to first list index
for wire in wires:
    wires[wire][0] = wire

# put first solution into b
wires['b'][0] = part1
    
print solve('a')