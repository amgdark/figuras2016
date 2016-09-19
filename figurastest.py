import unittest
from figuras import Figuras

class TestFiguras(unittest.TestCase):

	def setUp(self):
		self.figura = Figuras()

	def test_area_cuadrado_lado_6(self):
		resultado = self.figura.cuadrado(6)
		self.assertEqual(36,resultado)

	def test_area_cuadrado_lado_5(self):
		resultado = self.figura.cuadrado(5)
		self.assertEqual(25,resultado)

	def test_area_cuadrado_lado_g(self):
		resultado = self.figura.cuadrado('g')
		self.assertEqual('dato incorrecto',resultado)
			
	def tearDown(self):
		pass

if __name__ == '__main__':
	unittest.main()