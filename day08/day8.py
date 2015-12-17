#part 1 we cheat with eval() which pretty much converts our string to the desired format
#l[:-1] removes newline from end of input string
print sum(len(l[:-1])-len(eval(l)) for l in open('input.txt'))

#part 2 only need to count \'s and "'s and add 2 more for the surrounding quotes
print sum(len(filter(lambda x: x in ['\\','"'],l))+2 for l in open('input.txt'))