from string import replace
from random import shuffle

replacements = [a.strip().split() for a in open('input.txt').readlines()]

src = replacements.pop(len(replacements)-1)[0]
replacements.pop()

dest = set()

for a in range(len(replacements)):
    # j is pointing to the start of the unprocessed part of the string
    i = 0
    j = 0
    while replacements[a][0] in src[j:]:
        # find next place we can replace
        i = src[j:].index(replacements[a][0])
        # add to the set
        dest.add(src[:j + i] + replacements[a][2] + src[j + i + len(replacements[a][0]):])
        # update the search start pointer
        j = j + len(replacements[a][0])

print len(dest)

# sort replacements by length of replacement
replacements = sorted(replacements, key = lambda x: len(x[2]))[::-1]

a = 0
replaces = 0
src_bak = src
# greedily try the replacements from longest to shortest until we arrive at e (hopefully, or any 1 length result)
while len(src) > 1:
    if replacements[a][2] in src:
        replaces += src.count(replacements[a][2])
        src = replace(src, replacements[a][2], replacements[a][0])
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