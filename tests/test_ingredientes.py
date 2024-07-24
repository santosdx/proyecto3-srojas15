import unittest
import common.funciones as funciones
from models.ingredientes import Ingredientes


class TestIngredientes(unittest.TestCase):

    def test_es_sano_true(self):
        ingre_helado = Ingredientes("Helado Chocolate", 1800, 10, True, 50, "Chocolate")

        resultado = funciones.is_ingrediente_sano(ingre_helado.calorias, ingre_helado.vegetariano)
        self.assertEqual(resultado, True)

    def test_es_sano_false(self):
        ingre_helado = Ingredientes("Helado Chocolate", 1800, 120, False, 50, "Chocolate")
        resultado = funciones.is_ingrediente_sano(ingre_helado.calorias, ingre_helado.vegetariano)
        self.assertEqual(resultado, False)

    def test_abastecer_base(self):
        inventario = 5
        ingre_helado = Ingredientes("Helado Chocolate", 1800, 120, False, 5, "Chocolate")
        resultado = ingre_helado.inventario
        self.assertEqual(resultado, inventario)

    def test_renovar_complemento(self):
        inventario = 10
        ingre_helado = Ingredientes("Helado Chocolate", 1800, 120, False, 10, "Chocolate")
        resultado = ingre_helado.inventario
        self.assertEqual(resultado, inventario)
