lines = []

for l in open('input.txt').readlines():
    lines.append(l.strip().split())

def vm(r):
    pc = 0
    
    while 0 <= pc < len(lines):
        line = lines[pc]
        cmd = line[0]
        arg1 = line[1].strip(',')
        if len(line) > 2:
            arg2 = line[2]
            
        if cmd == 'hlf':
            r[arg1] /= 2
        elif cmd == 'tpl':
            r[arg1] *= 3
        elif cmd == 'inc':
            r[arg1] += 1
        # to save a few lines, pc is incremented every time so jumps are tuned 1 instruction back
        elif cmd == 'jmp':
            pc = pc + int(arg1) - 1
        elif cmd == 'jie' and r[arg1] %2 == 0:
            pc = pc + int(arg2) - 1
        elif cmd == 'jio' and r[arg1] == 1:
            pc = pc + int(arg2) - 1
        pc += 1
    return r['b']
    
print vm({'a': 0, 'b': 0}), vm({'a': 1, 'b': 0})