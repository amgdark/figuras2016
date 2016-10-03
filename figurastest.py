import unittest
from figuras import Figuras


class TestFiguras(unittest.TestCase):

    def setUp(self):
        self.figura = Figuras()

    def test_area_cuadrado_lado_6(self):
        self.cuadrado(6, 36)

    def test_area_cuadrado_lado_5(self):
        self.cuadrado(5, 25)

    def test_area_cuadrado_lado_7(self):
        self.cuadrado(7, 49)

    def test_area_cuadrado_lado_g(self):
        self.cuadrado('g', 'dato incorrecto')

    def cuadrado(self, lado, esperado):
        resultado = self.figura.cuadrado(lado)
        self.assertEqual(resultado, esperado)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
