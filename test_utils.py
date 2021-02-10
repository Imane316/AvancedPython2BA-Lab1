# test_utils.py
# Author: Sébastien Combéfis
# Version: February 8, 2018

import unittest
import utils

class TestUtils(unittest.TestCase):
    def test_fact(self):
        self.assertEqual(utils.fact(5), 120)
        self.assertEqual(utils.fact(2), 2)
        pass
    
    def test_roots(self):
        self.assertEqual(utils.roots(1,3,2), (1,2))
        self.assertEqual(utils.roots(1,5,6), (2,3))
        pass
    
    def test_integrate(self):
        # À compléter...
        pass

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestUtils)
    runner = unittest.TextTestRunner()
    exit(not runner.run(suite).wasSuccessful())
