import unittest 
from gpt4 import suma
from gpt4 import average

class TestMain(unittest.TestCase):
    
    def test_suma(self):
        self.assertEqual(suma(5,7),12)
        self.assertEqual(suma(-1,1),0)
        self.assertEqual(suma(5.5,6.3),11.8)

    def test_average(self):
        score = [2,2,2]
        self.assertEqual(average(score),2)
    
    
    