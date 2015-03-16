import string
import sys
from collections import Counter
from string import ascii_lowercase

# For testing!
raw = open("beautiful string.txt");
test_cases = raw.read().strip().splitlines();
print test_cases

# with open(sys.argv[1], 'r') as input:
#     test_cases = input.read().strip().splitlines()

for test in test_cases:
    string = [i.lower() for i in test if i.lower() in ascii_lowercase]
    count = Counter(string)
    print count
    key = dict()
    beauty = 26
    for i in count.most_common():
    	print i
        key[i[0]] = beauty
        beauty -= 1
    print sum(key.get(i, 0) for i in string)