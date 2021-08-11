import unittest

from sorted_frozen_set import SortedFrozenSet


class TestConstruction(unittest.TestCase):

    def test_construct_empty(self):
        s = SortedFrozenSet([])

    def test_construct_from_non_empty_list(self):
        items = [7, 6, 8, 4]
        s = SortedFrozenSet(items)

    def test_construct_from_an_iterator(self):
        items = [7, 6, 8, 4]
        iterator = iter(items)
        s = SortedFrozenSet(iterator)

    def test_construct_no_args(self):
        s = SortedFrozenSet()


if __name__ == "__main__":
    unittest.main()
