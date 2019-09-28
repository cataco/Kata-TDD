from unittest import TestCase

from Calculadora import Calculadora


class TestCalculadora(TestCase):
    def testSumar(self):
        self.assertEqual(Calculadora().sumar(""), 0, "empty")

    def testSumarUno(self):
        self.assertEqual(Calculadora().sumar("1"), 1, "empty")

    def testSumarNumero(self):
        self.assertEqual(Calculadora().sumar("1"), 1, "empty")
        self.assertEqual(Calculadora().sumar("2"), 2, "empty")