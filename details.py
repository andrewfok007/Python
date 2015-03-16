import sys

with open(sys.argv[1], 'r') as input:
    test_cases = input.read().strip().splitlines()
    
test_cases = filter(None, test_cases)

for el in test_cases:
    a=[]
    li = el.split(',')
    for i in li:
        a.append(i.count('.'))
    print min(a)
        
        
