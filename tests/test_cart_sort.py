import unittest

from aims.cart import Cart
from aims.dvd import DigitalVideoDisc


class TestCartSort(unittest.TestCase):

    def setUp(self):
        self.cart = Cart()
        self.dvd1 = DigitalVideoDisc("Zootopia", cost=20)
        self.dvd2 = DigitalVideoDisc("Avengers", cost=30)
        self.dvd3 = DigitalVideoDisc("Frozen", cost=10)

        self.cart.items = [self.dvd1, self.dvd2, self.dvd3]

    def test_sort_by_title(self):
        self.cart.sort_by_title()

        titles = [dvd.title for dvd in self.cart.items]
        self.assertEqual(titles, ["Avengers", "Frozen", "Zootopia"])

    def test_sort_by_cost(self):
        self.cart.sort_by_cost()

        costs = [dvd.cost for dvd in self.cart.items]
        self.assertEqual(costs, [10, 20, 30])


if __name__ == "__main__":
    unittest.main()