import unittest
from main import suma,resta,multiplicacion,division

class Test(unittest.TestCase):
    
    def test(self):
        self.assertEqual(suma(3,2), 5)
        self.assertEqual(suma(-1,1), 0)
        self.assertEqual(suma(-1,-1), -2)

        self.assertEqual(resta(2,1), 1)
        self.assertEqual(resta(5,2), 3)
        self.assertEqual(resta(1,2), -1)

        self.assertEqual(multiplicacion(10,5), 50)
        self.assertEqual(multiplicacion(3,3), 9)
        self.assertEqual(multiplicacion(3,2), 6)

        self.assertEqual(division(1,1), 1)
        self.assertEqual(division(25,5), 5)
        self.assertEqual(division(5,0), 0)

if __name__ == '__main__':
    unittest.main()