from re import findall

compounds={'children': 3, 'cats': 7, 'samoyeds': 2, 'pomeranians': 3, 'akitas': 0, 'vizslas': 0, 'goldfish': 5, 'trees': 3, 'cars': 2, 'perfumes': 1}

for l in open('input.txt'):
    a = findall('(\d+): (.+): (\d+), (.+): (\d+), (.+): (\d+)', l.strip())[0]
    valid1 = 1
    valid2 = 1
    
    #loop the 3 compounds we know about each aunt
    for compound in range(1,6,2):
    
        amount=int(a[compound+1])
        
        #part1 check
        if compounds[a[compound]] != amount:
            valid1 = 0
        
        #part2 checks
        #using a list to check is more compact than chained comparisons
        if a[compound] in ['cats','trees']:
            if compounds[a[compound]] >= amount:
                valid2 = 0
        elif a[compound] in ['pomeranians','goldfish']:
            if compounds[a[compound]] <= amount:
                valid2 = 0
        elif compounds[a[compound]] != amount:
            valid2 = 0
            
    if valid1:
        print 'Part 1:', a[0]
    if valid2:
        print 'Part 2:', a[0]

