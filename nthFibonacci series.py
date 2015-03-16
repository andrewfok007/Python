import sys
import math
import unittest
with open(sys.argv[1], 'r') as input:
    test_cases = input.read().strip().splitlines()

# Recursion method - O(2^n)
# def go(test):
#     if test == 0:
#         return 0;
#     elif test == 1:
#         return 1;
#     else:
#         return go(test-1)+go(test-2)

# Cheat method using exact formula
# def F(n):
#     return ((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5))

def fib():
    a, b = 0, 1
    while True:            # First iteration:
        yield a            # yield 0 to start with and then
        a, b = b, a + b    # a will now be 1, and b will also be 1, (0 + 1)

def go(test):
    test = int(test);
    for index, fibonacci_number in enumerate(fib()):
        if test == 0:
            print 0;
        elif index == test:
             print fibonacci_number;


# test = 12;
# go(test);

for test in test_cases:
	go(test);

# class TestSequenceFunctions(unittest.TestCase):
#     def setUp(self):
#         self.seq1 = 0
#         self.seq2 = 5
#         self.seq3 = 12
#     def test_shuffle(self):
#         # make sure the shuffled sequence does not lose any elements
#         self.assertEqual(go(self.seq1), 0)
#         self.assertEqual(go(self.seq2), 5)
#         self.assertEqual(go(self.seq3), 144)
# if __name__ == '__main__':
#     unittest.main()