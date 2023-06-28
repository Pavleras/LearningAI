import unittest

def sumar(a,b):
    return a + b

def parImpar(n):
    return n % 2 == 0

class TestSumar(unittest.TestCase):
    def test_sumar_positivos_OK(self):
        self.assertEquals(sumar(2,2),4)
    def test_sumar_negativos_OK(self):
        self.assertEqual(sumar(-2,-5),-7)
    def test_sumar_negativos_NO(self):
        self.assertNotEqual(sumar(-2,-5),7)    
    def test_es_par(self):
        self.assertTrue(parImpar(2))
    def test_es_par_NO(self):
        self.assertFalse(parImpar(1))
    
if __name__ == '__main__':
    unittest.main()