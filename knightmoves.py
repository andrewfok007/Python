import sys
import string
import itertools

with open(sys.argv[1], 'r') as input:
    test_cases = input.read().strip().splitlines()
    
test_cases = filter(None, test_cases)

#print test_cases

cb = [['a8','b8','c8','d8','b8'], ['a7', 'b7']]
print list(string.lowercase[:8])
