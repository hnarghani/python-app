import unittest
from app import add
class TestApp(unittest.TestCase):
    def add_test(self):
        self.assertEqual((add(1,2) , 3))
        self.assertEqual((add(3,4) , 7))
        self.assertEqual((add(1,-1) , 0))
if __name__ == "__main__":
    unittest.main()


