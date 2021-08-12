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


class TestContainerProtocol(unittest.TestCase):

    # Method used to prepare the test context. In this example is used
    # to attach text fixtures to the test instance self.
    def setUp(self):
        self.s = SortedFrozenSet([6, 7, 3, 9])

    def test_positive_contain(self):
        self.assertTrue(6 in self.s)

    def test_negative_contain(self):
        self.assertFalse(2 in self.s)

    def test_positive_not_contained(self):
        self.assertTrue(5 not in self.s)

    def test_negative_not_contained(self):
        self.assertFalse(9 not in self.s)


if __name__ == "__main__":
    unittest.main()
