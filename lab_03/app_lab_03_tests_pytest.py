
import pytest
from app_lab_03 import Product

@pytest.fixture
def default_product():
    return Product("Laptop", 3000.0, 5)

def test_is_available_returns_false_for_empty_product():
    empty_product = Product("Czekolada", 5.0, 0)
    assert empty_product.is_available() is False

def test_is_available_returns_true_for_stocked_product(default_product):
    assert default_product.is_available() is True

def test_add_stock_increases_quantity(default_product):
    default_product.add_stock(10)
    assert default_product.quantity == 15

def test_remove_stock_decreases_quantity(default_product):
    default_product.remove_stock(2)
    assert default_product.quantity == 3

def test_total_value_calculation(default_product):
    assert default_product.total_value() == 15000.0

def test_init_raises_value_error_for_negative_price():
    with pytest.raises(ValueError, match="Cena nie może być ujemna"):
        Product("Błędny produkt", -10.0, 5)

def test_remove_stock_raises_value_error_for_insufficient_funds(default_product):
    with pytest.raises(ValueError, match="Brak wystarczającej ilości towaru"):
        default_product.remove_stock(10)

def test_add_stock_raises_value_error_for_negative_amount(default_product):
    with pytest.raises(ValueError, match="Nie można dodać ujemnej ilości"):
        default_product.add_stock(-5)