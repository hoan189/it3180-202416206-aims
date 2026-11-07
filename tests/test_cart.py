import unittest
from aims.cart import Cart
from aims.dvd import DigitalVideoDisc


class TestCart(unittest.TestCase):
    def test_add_dvd_until_full(self):
        cart = Cart()

        for i in range(20):
            dvd = DigitalVideoDisc(f"DVD {i}", "Test", "Author", 100, 10)
            self.assertTrue(cart.add_dvd(dvd))

        dvd = DigitalVideoDisc("DVD 21", "Test", "Author", 100, 10)
        self.assertFalse(cart.add_dvd(dvd))


if __name__ == "__main__":
    unittest.main()