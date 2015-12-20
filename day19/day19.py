from string import replace
from random import shuffle
from re import findall

replacements = [a for a in findall(r'(\w+) => (\w+)',open('input.txt').read())]

src = open('input.txt').readlines()[-1]

dest = set()

for replacement in replacements:
    # j is pointing to the start of the unprocessed part of the string
    i = 0
    j = 0
    while replacement[0] in src[j:]:
        # find next place we can replace
        i = src[j:].index(replacement[0])
        # add to the set
        dest.add(src[:j + i] + replacement[1] + src[j + i + len(replacement[0]):])
        # update the search start pointer
        j = j + len(replacement[0])

print len(dest)

# sort replacements by length of replacement
replacements = sorted(replacements, key = lambda x: len(x[1]))[::-1]

a = 0
replaces = 0
src_bak = src
# greedily try the replacements from longest to shortest until we arrive at e (hopefully, or any 1 length result)
while len(src) > 1:
    if replacements[a][1] in src:
        replaces += src.count(replacements[a][1])
        src = replace(src, replacements[a][1], replacements[a][0])
        a = 0
    else:
        a += 1
    # the greedy algorithm was proven to fail in some cases, plan B is to randomize replacements until we succeed
    if a > len(replacements)-1:
        src = src_bak
        shuffle(replacements)
        a = 0
        replaces = 0

print replaces