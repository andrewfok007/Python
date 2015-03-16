import sys

with open(sys.argv[1], 'r') as input:
    test_cases = input.read().strip().splitlines()

# For testing!
# import unittest
# raw = open("maxrangesum.txt");
# test_cases = raw.read().strip().splitlines();
# print test_cases

def go(test):
	days, gains = test.split(";");
	gain = [int(i) for i in gains.split()];
	day = int(days);
	# print day, gain, gain[0:5];
	i=0; current=0;
	while i + day <= len(gain):
		update = sum(gain[i:day+i]);
		# print update;
		if update <= 0:
			update = 0;
		if update>current:
			current = update;
		i+=1;
	# return current;
	print current;

for test in test_cases:
	go(test);

# class TestSequenceFunctions(unittest.TestCase):
#     def setUp(self):
#         self.seq1 = '5;7 -3 -10 4 2 8 -2 4 -5 -2'
#         self.seq2 = '6;-4 3 -10 5 3 -7 -3 7 -6 3'
#         self.seq3 = '3;-7 0 -45 34 -24 7'
#     def test_shuffle(self):
#         # make sure the shuffled sequence does not lose any elements
#         self.assertEqual(go(self.seq1), 16)
#         self.assertEqual(go(self.seq2), 0)
#         self.assertEqual(go(self.seq3), 17)
# if __name__ == '__main__':
#     unittest.main()


# #Alternative solution
# with open(sys.argv[1], 'rb') as test_cases:
#     for test in test_cases:
#         n, ls = test.split(';')
#         n, ls = int(n), map(int, ls.split())
#         m = s = sum(ls[:n])

#         for i, e in enumerate(ls[n:], n):
#             s += (e - ls[i - n])
#             m = max(m, s)
#         print(max(m, 0))