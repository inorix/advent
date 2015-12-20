from string import ascii_lowercase
from re import findall,sub

def find_pass(input):
    abc = ascii_lowercase
    rule1 = '|'.join([x + y + z for x, y, z in zip(abc[:-2], abc[1:], abc[2:])])
    rule2 = 'i|o|l'
    rule3 = '|'.join([x + y for x, y in zip(abc, abc)])
    
    while True:
        input = sub('([a-y])(z*)$', lambda x: chr(ord(x.group(1)) + 1) + len(x.group(2)) * 'a', input)
        if len(findall(rule1, input)) and not len(findall(rule2, input)) and len(findall(rule3, input)) > 1:
            yield input
      
passwords = find_pass('hxbxwxba')
print passwords.next(), passwords.next()
