import unittest
from aims.dvd import DigitalVideoDisc
from aims.search import search_by_category


class TestSearchByCategory(unittest.TestCase):
    def setUp(self):
        self.dvds = [
            DigitalVideoDisc("The Lion King", category="Animation"),
            DigitalVideoDisc("Avengers", category="Action"),
            DigitalVideoDisc("Frozen", category="Animation"),
        ]

    def test_search_by_category(self):
        result = search_by_category(self.dvds, "animation")
        titles = [dvd.title for dvd in result]

        self.assertEqual(titles, ["The Lion King", "Frozen"])


if __name__ == "__main__":
    unittest.main()