from re import findall
from json import loads

input = open('input.txt').read()

print sum(map(int, findall('[-0-9]+', input)))

def hook(obj):
    return {} if 'red' in obj.values() else obj

#part 2 is using json.loads() object_hook to filter out objects containing red. credit to /u/meithan    
print sum(map(int, findall('[-0-9]+', str(loads(input, object_hook=hook)))))
