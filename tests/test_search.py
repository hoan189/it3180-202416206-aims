import unittest
from aims.search import search_by_title
from aims.dvd import DigitalVideoDisc


class TestSearch(unittest.TestCase):
    def setUp(self):
        self.dvds = [
            DigitalVideoDisc("The Lion King", "Animation", "Roger", 100, 10),
            DigitalVideoDisc("Frozen", "Animation", "Chris", 90, 10),
        ]

    def test_search_by_title(self):
        result = search_by_title(self.dvds, "lion")

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].title, "The Lion King")

    def test_search_by_title_uppercase(self):
        result = search_by_title(self.dvds, "LION")

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].title, "The Lion King")

    def test_search_by_title_mixed_case(self):
        result = search_by_title(self.dvds, "LiOn")

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].title, "The Lion King")

    def test_search_by_title_not_found(self):
        result = search_by_title(self.dvds, "Avatar")

        self.assertEqual(len(result), 0)


if __name__ == "__main__":
    unittest.main()