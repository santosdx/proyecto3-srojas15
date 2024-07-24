import unittest
import common.funciones as funciones
from models.ingredientes import Ingredientes
from models.productos import Productos
from models.heladeria import Heladeria
from app import app


class TestProductos(unittest.TestCase):

    def setUp(self):
        self.app_context = app.app_context()
        self.app_context.push()

    def test_calcular_caloria_copa(self):

        ingre_helado = Ingredientes("Helado Chocolate", 1800, 200, True, 50, "Chocolate")
        ingre_crema = Ingredientes("Crema chantilli", 700, 100, True, 50, "")

        lista_ingredientes = [ingre_helado, ingre_crema]

        copa_helado_chocolate = Productos("Copa helado chocolate", 10000, "Galleta", 70, lista_ingredientes)

        resultado = copa_helado_chocolate.calcular_calorias()
        self.assertEqual(resultado,  285.0)

    def test_calcular_caloria_malteada(self):

        ingre_helado = Ingredientes("Helado Chocolate", 1800, 200, True, 50, "Chocolate")
        ingre_crema = Ingredientes("Crema chantilli", 700, 100, True, 50, "")

        lista_ingredientes = [ingre_helado, ingre_crema]

        copa_helado_chocolate = Productos("Copa helado chocolate", 10000, None, 70, lista_ingredientes)

        resultado = copa_helado_chocolate.calcular_calorias()
        self.assertEqual(resultado,  500)

    def test_calcular_costo_produccion_copa(self):

        ingre_helado = Ingredientes("Helado Chocolate", 1800, 200, True, 50, "Chocolate")
        ingre_crema = Ingredientes("Crema chantilli", 700, 100, True, 50, "")

        lista_ingredientes = [ingre_helado, ingre_crema]

        copa_helado_chocolate = Productos("Copa helado chocolate", 10000, "Galleta", 70, lista_ingredientes)

        resultado = copa_helado_chocolate.calcular_costo()
        self.assertEqual(resultado,  2500.0)

    def test_calcular_costo_produccion_malteada(self):

        ingre_helado = Ingredientes("Helado Chocolate", 1800, 200, True, 50, "Chocolate")
        ingre_crema = Ingredientes("Crema chantilli", 700, 100, True, 50, "")

        lista_ingredientes = [ingre_helado, ingre_crema]

        copa_helado_chocolate = Productos("Copa helado chocolate", 10000, None, 70, lista_ingredientes)

        resultado = copa_helado_chocolate.calcular_costo()
        self.assertEqual(resultado,   3000.0)

    def test_calcular_rentabilidad(self):

        ingre_helado = Ingredientes("Helado Chocolate", 1800, 200, True, 50, "Chocolate")
        ingre_crema = Ingredientes("Crema chantilli", 700, 100, True, 50, "")

        lista_ingredientes = [ingre_helado, ingre_crema]

        copa_helado_chocolate = Productos("Copa helado chocolate", 10000, None, 70, lista_ingredientes)

        resultado = copa_helado_chocolate.calcular_rentabilidad()
        self.assertEqual(resultado,   7500.0)

    def test_producto_mas_rentable(self):

        ingre_helado = Ingredientes("Helado Chocolate", 1800, 200, True, 50, "Chocolate")
        ingre_crema = Ingredientes("Crema chantilli", 700, 100, True, 50, "")
        ingre_cono = Ingredientes("Cono de galleta", 250, 2, True, 150, "")

        lista_ingredientes1 = [ingre_helado, ingre_crema]
        lista_ingredientes2 = [ingre_helado, ingre_crema, ingre_cono]

        copa_helado_chocolate = Productos("Copa helado chocolate", 10000, None, 70, lista_ingredientes1)
        malteada_frutos = Productos("Malteada frutos rojos", 15700, None, 120, lista_ingredientes2)

        lista_productos = [copa_helado_chocolate, malteada_frutos]

        resultado = funciones.producto_mas_rentable(lista_productos)
        self.assertEqual(resultado,   "['Malteada frutos rojos']")

    def test_vender(self):

        la_heladeria = Heladeria("La Heladeria")
        producto = 'Copa helado gelatina'
        resultado = la_heladeria.vender(producto)

        self.assertEqual(resultado, "¡Vendido!")

    def test_vender_error(self):

        la_heladeria = Heladeria("La Heladeria")
        producto = 'Malteada frutos rojos'

        self.assertRaises(ValueError, la_heladeria.vender, producto)
