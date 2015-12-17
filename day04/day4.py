import md5

input = 'iwrupvqb'
target = '00000'
c = 0

while md5.new(input + str(c)).digest().encode('hex')[:5] != target:
    c += 1
print c
target += '0'
while md5.new(input + str(c)).digest().encode('hex')[:6] != target:
    c += 1
print c
