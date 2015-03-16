import sys

with open(sys.argv[1], 'r') as input:
    test_cases = input.read().strip().splitlines()

# raw = open("fizzbizz.txt");
# test_cases = raw.read().strip().splitlines();
print test_cases

for test in test_cases:
    fizz, buzz, limit = (int(i) for i in test.split())
    fizzes = {i * fizz for i in xrange(1, limit/fizz + 1)}
    buzzes = {i * buzz for i in xrange(1, limit/buzz + 1)}
    for i in xrange(1, limit + 1):
        if i in fizzes & buzzes:
            print 'FB',
        elif i in fizzes:
            print 'F',
        elif i in buzzes:
            print 'B',
        else:
            print i,
    print
