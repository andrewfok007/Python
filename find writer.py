import sys

# with open(sys.argv[1], 'r') as input:
#     test_cases = input.read().strip().splitlines()

raw = open("find writer.txt");
test_cases = raw.read().strip().splitlines();
print test_cases

for test in test_cases:
    if test:
        code, key = test.split('|')
        print ''.join((code[i - 1] for i in (int(n) for n in key.split())))
        
# the numbers on rhs are the index locations of the code on lhs, so number 3 means code[3-1] = S