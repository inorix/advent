from re import finditer

input = '1113222113'

for i in range(50):
    #match any digit and any consecutive same digit
    #loop over matches, create count+digit strings for each, glue them together
    input = ''.join(map(lambda x: str(len(x)) + x[0], [b.group(0) for b in finditer(r'(\d)\1{0,9}',input)]))
    if i==39 or i==49:
        print len(input)
