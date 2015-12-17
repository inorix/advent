from re import findall,search

#both generators filter for only the nice strings
print len([s for s in open('input.txt').readlines() if len(findall(r'[aeiou]', s)) > 2 and search(r'(.)\1+', s) and not search(r'ab|cd|pq|xy', s)])
print len([s for s in open('input.txt').readlines() if search(r'(..).*\1', s) and search(r'(.).\1', s)])
