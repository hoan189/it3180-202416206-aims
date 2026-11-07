import unittest
from aims.search import search_by_title
from aims.dvd import DigitalVideoDisc


class TestSearch(unittest.TestCase):
    def test_search_by_title(self):
        dvds = [
            DigitalVideoDisc("The Lion King", "Animation", "Roger", 100, 10),
            DigitalVideoDisc("Frozen", "Animation", "Chris", 90, 10),
        ]

        result = search_by_title(dvds, "lion")

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].title, "The Lion King")


if __name__ == "__main__":
    unittest.main()