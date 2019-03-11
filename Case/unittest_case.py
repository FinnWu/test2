import unittest

class FirstUnittest(unittest.TestCase):

    def setUp(self):
        print("这是前置条件")
    def tearDown(self):
        print("这是后置条件")
    def testq1(self):
        print('1')
    def q2(self):
        print('2')

if __name__ == "__main__":
    unittest.main()