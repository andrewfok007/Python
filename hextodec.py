import sys
import math
import unittest
# with open(sys.argv[1], 'r') as input:
#     test_cases = input.read().strip().splitlines()

def go(test):
	# print int(test, 16);
    return int(test, 16);

test = '35';
print go(test);

# for test in test_cases:
# 	go(test);

class TestSequenceFunctions(unittest.TestCase):
    def setUp(self):
        self.seq1 = '9f'
        self.seq2 = '11'
    def test_shuffle(self):
        # make sure the shuffled sequence does not lose any elements
        self.assertEqual(go(self.seq1), 159)
        self.assertEqual(go(self.seq2), 17)
if __name__ == '__main__':
    unittest.main()