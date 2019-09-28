from unittest import TestCase

import Calculadora


class TestCalculadora(TestCase):
    def testSumar(self):
        self.assertEqual(Calculadora.sumar(""), 0, "empty")
