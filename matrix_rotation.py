import sys
import math
import unittest
# with open(sys.argv[1], 'r') as input:
#     test_cases = input.read().strip().splitlines()

# For testing!
# raw = open("maxrangesum.txt");
# test_cases = raw.read().strip().splitlines();
# print test_cases

def chunks(l, n):
    """ Yield successive n-sized chunks from l."""
    for i in xrange(0, len(l), n):
        yield l[i:i+n]

def go(test):
	test = test.split();
	n = int(math.sqrt(len(test)));
	a = list(chunks(test, n));
	b = list(chunks([0]*len(test), n));

	for i in range(0,n):
		for j in range(0,n):
			b[j][n-1-i] = a[i][j];

	for i in range(0,n):
		b[i] = ' '.join(b[i])
	b = ' '.join(b)
	print b
	return b

# test = 'a b c d';
# go(test);

# for test in test_cases:
# 	go(test);

class TestSequenceFunctions(unittest.TestCase):
    def setUp(self):
        self.seq1 = 'a b c d'
        self.seq2 = 'a b c d e f g h i j k l m n o p'
        self.seq3 = 'a b c d e f g h i'
    def test_shuffle(self):
        # make sure the shuffled sequence does not lose any elements
        self.assertEqual(go(self.seq1), 'c a d b')
        self.assertEqual(go(self.seq2), 'm i e a n j f b o k g c p l h d')
        self.assertEqual(go(self.seq3), 'g d a h e b i f c')
if __name__ == '__main__':
    unittest.main()