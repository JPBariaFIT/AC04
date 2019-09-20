from unittest import TestCase
from com.baria.operacoes import Operacoes
 
class TestOperacoes(TestCase):

    def setUp(self):
        self.operacoes = Operacoes()

    def test_mult(self):
        self.assertEqual(self.operacoes.mult([1,2]), 2)