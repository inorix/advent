from math import sqrt

# calculate factors to sqrt(x) and their corresponding pairs
def divisors(x):
    divisors = []
    for i in xrange(1, int(sqrt(x) + 1)):
        if x % i == 0:
            yield i
            if i * i != x:
                yield (x / i)

target = 33100000
part1 = False
part2 = False

a = 1

while not part1 or not part2:
    a += 1
    d = list(divisors(a))
    result = sum(d) * 10
    if part1 == 0 and result > target:
        print a
        part1 = True
    # filter divisors for part 2
    result = sum([b for b in d if b * 50 > a]) * 11
    if part2 == 0 and result > target:
        print a
        part2 = True
