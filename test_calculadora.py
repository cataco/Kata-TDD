from unittest import TestCase

from Calculadora import Calculadora


class TestCalculadora(TestCase):
    def testSumar(self):
        self.assertEqual(Calculadora().sumar(""), 0, "empty")
