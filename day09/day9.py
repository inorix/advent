from itertools import permutations
from re import findall
from collections import defaultdict

distances = defaultdict(dict)
cities = set()

for l in open('input.txt'):
    a = findall(r'(.+) to (.+) = (\d+)', l)[0]
    #cities is a set so cannot have duplicates, no need to check if city is in there
    cities.add(a[0])
    cities.add(a[1])
    distances[a[0]][a[1]] = int(a[2])
    distances[a[1]][a[0]] = int(a[2])

#loop over all permutations, add the distances together and store the result in a list
#solution is generic, works with any number of cities
res = [sum([distances[route[city]][route[city+1]] for city in range(len(route)-1)]) for route in permutations(cities)]

print min(res), max(res)