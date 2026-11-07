import unittest
from aims.cart import Cart
from aims.dvd import DigitalVideoDisc


class TestDiscount(unittest.TestCase):
    def test_discount_20_percent(self):
        cart = Cart()
        dvd = DigitalVideoDisc("Test", "Test", "Author", 100, 100)
        cart.add_dvd(dvd)

        self.assertEqual(cart.total_cost_after_discount(20), 80)

    def test_invalid_discount(self):
        cart = Cart()

        with self.assertRaises(ValueError):
            cart.total_cost_after_discount(150)


if __name__ == "__main__":
    unittest.main()