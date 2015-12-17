from re import findall

properties = []

for l in open('input.txt').readlines():
    properties.append(map(int, findall('([-0-9]+)', l)))

part1 = 0
part2 = 0

#loop over each ingredient configuration that adds up to 100
#works well with such a small input, two ingredients more or a higher total amount would make this approach run forever
for sprinkles in range(101):
    for butterscotch in range(101-sprinkles):
        for chocolate in range(101-sprinkles-butterscotch):
            candy = 100-sprinkles-butterscotch-chocolate
            
            s = []
            
            #loop over each property of all ingredients
            for index,property in enumerate(zip(*properties)):
                #multiply the property with the corresponding amount
                cur = sum(map(lambda x, y: x * y, [sprinkles, butterscotch, chocolate, candy], property))
                #do not add calories
                if index < 4:
                    #negative score zeroes the result, so replace negative score with zero
                    s.append(max(cur,0))
            
            #multiply it all together
            s = reduce(lambda x, y: x * y, s)
            
            if s > part1:
            part1 = max(part1, s)
            if g == 500:
                part2 = max(part2, s)
            
print part1,part2
