'''
Escribe una función que tome una lista de números y devuelva una nueva lista que contenga sólo los números pares de la lista original, en el mismo orden.
'''

import unittest

def esPar(numero):
    return numero % 2 == 0

def process(list):
    listapares = []
    for num in list:
        if esPar(num):
            listapares.append(num)
    return listapares

class Test(unittest.TestCase):
    def test_getEvenNumberIsOk(self):
        newlist = {2,3,5,7,8}
        self.assertEqual(len(process(newlist)),2)
    def test_esPar(self):
        self.assertEqual(esPar(2),True)
    def test_esImpar(self):
        self.assertEqual(esPar(3),False)
    def test_evenNumberIsOk(self):
        newlist = {1,2,3}
        lista = process(newlist)
        self.assertEqual(lista.count(2),1)
    def test_getEvenNumberIsOk(self):
        self.assertEqual(process({1,2,3}).pop(0),2)
    

if __name__ == '__main__':
    unittest.main()