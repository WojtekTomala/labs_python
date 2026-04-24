import unittest
from app_lab_03 import Product

class TestProduct(unittest.TestCase):

    def setUp(self):
        self.product = Product("Laptop", 3000.0, 5)

    def test_is_available_returns_false_for_empty_product(self):
        empty_product = Product("Klawiatura", 150.0, 0)
        self.assertFalse(empty_product.is_available())

    def test_is_available_returns_true_for_stocked_product(self):
        self.assertTrue(self.product.is_available())

    def test_add_stock_increases_quantity(self):
        self.product.add_stock(10)
        self.assertEqual(self.product.quantity, 15)

    def test_remove_stock_decreases_quantity(self):
        self.product.remove_stock(2)
        self.assertEqual(self.product.quantity, 3)

    def test_total_value_calculation(self):
        self.assertEqual(self.product.total_value(), 15000.0)

    def test_init_raises_value_error_for_negative_price(self):
        with self.assertRaises(ValueError):
            Product("Błędny produkt", -10.0, 5)

    def test_remove_stock_raises_value_error_for_insufficient_funds(self):
        with self.assertRaises(ValueError):
            self.product.remove_stock(10)

    def test_add_stock_raises_value_error_for_negative_amount(self):
        with self.assertRaises(ValueError):
            self.product.add_stock(-5)

if __name__ == '__main__':
    unittest.main()