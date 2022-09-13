import unittest
import state

class StateTest(unittest.TestCase):

    def testhdistance1A(self):
        # test func that finds number of tiles out of place
        s = [0, 2, 1, 3]
        actual = state.hdistance1(s)
        expected = 2
        self.assertEqual(expected, actual)
    
    def testhdistance1B(self):
        # test func that finds number of tiles out of place
        s = [0, 1, 2, 3]
        actual = state.hdistance1(s)
        expected = 0
        self.assertEqual(expected, actual)

    def testhdistance1C(self):
        # test func that finds number of tiles out of place
        s = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        actual = state.hdistance1(s)
        expected = 0
        self.assertEqual(expected, actual)

    def testhdistance1D(self):
        # test func that finds number of tiles out of place
        s = [6, 1, 7, 4, 3, 2, 8, 5, 0]
        actual = state.hdistance1(s)
        expected = 7
        self.assertEqual(expected, actual)
    
    def testhdistance1E(self):
        # test func that finds number of tiles out of place
        s = [6, 1, 2, 4, 3, 5, 8, 7, 0]
        actual = state.hdistance1(s)
        expected = 4
        self.assertEqual(expected, actual)

    def testhdistance1F(self):
        # test func that finds number of tiles out of place
        s = [0, 1, 5, 3, 4, 2, 6, 7, 8]
        actual = state.hdistance1(s)
        expected = 2
        self.assertEqual(expected, actual)
    
    def testhdistance1G(self):
        # test func that finds number of tiles out of place
        s = [7, 2, 4, 5, 0, 6, 8, 3, 1]
        actual = state.hdistance1(s)
        expected = 8
        self.assertEqual(expected, actual)

    def testhdistance1H(self):
        # test func that finds number of tiles out of place
        s = range(16)
        actual = state.hdistance1(s)
        expected = 0
        self.assertEqual(expected, actual)
    
    def testhdistance1I(self):
        # test func that finds number of tiles out of place
        s = list(range(16))
        s[4] = 2
        s[2] = 4
        actual = state.hdistance1(s)
        expected = 2
        self.assertEqual(expected, actual)

    def testhdistance2A(self):
        #test func that calculates manhattan dist
        s = [0, 1, 2, 3]
        actual = state.hdistance2(s)
        expected = 0
        self.assertEqual(expected, actual)
    
    def testhdistance2B(self):
        #test func that calculates manhattan dist
        s = [0, 2, 1, 3]
        actual = state.hdistance2(s)
        expected = 4
        self.assertEqual(expected, actual)
    
    def testhdistance2C(self):
        #test func that calculates manhattan dist
        s = [7, 2, 4, 5, 0, 6, 8, 3, 1]
        actual = state.hdistance2(s)
        expected = 18
        self.assertEqual(expected, actual)
    
    def testhdistance2D(self):
        #test func that calculates manhattan dist
        s = range(16)
        actual = state.hdistance2(s)
        expected = 0
        self.assertEqual(expected, actual)

    def testhdistance2E(self):
        #test func that calculates manhattan dist
        s = list(range(16))
        s[5] = 10
        s[10] = 5
        actual = state.hdistance2(s)
        expected = 4
        self.assertEqual(expected, actual)    

    def testhdistance2F(self):
        #test func that calculates manhattan dist
        s = list(range(16))
        s[1] = 15
        s[15] = 1
        actual = state.hdistance2(s)
        expected = 10
        self.assertEqual(expected, actual)
    
if __name__ == '__main__':
    unittest.main()