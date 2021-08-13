from collections.abc import Sequence
from itertools import chain


# This class inherits from Sequence getting
# access to the index method
class SortedFrozenSet(Sequence):

    def __init__(self, item=None):
        self._items = tuple(sorted(
            set(item) if (item is not None)
            else set()
        ))

    # This special method accepts a single argument which is the item
    # for which to test for containment, and returns a boolean
    def __contains__(self, item):
        return item in self._items

    # Size protocol
    def __len__(self):
        return len(self._items)

    def __iter__(self):
        return iter(self._items)

    def __getitem__(self, index):
        result = self._items[index]
        return (
            SortedFrozenSet(result) if isinstance(index, slice)
            else result
        )

    def __repr__(self):
        return "{type}({arg})".format(
            type=type(self).__name__,
            arg=(
                "[{}]".format(
                    ", ".join(
                        map(repr, self._items)
                    )
                )
                if self._items else ""
            )
        )

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented
        return self._items == other._items

    def __hash__(self):
        return hash(
            (type(self), self._items)
        )

    def __add__(self, rhs):
        if not isinstance(rhs, type(self)):
            return NotImplemented
        return SortedFrozenSet(
            chain(self._items, rhs._items)
        )

    def __mul__(self, rhs):
        return self if rhs > 0 else SortedFrozenSet()

    def __rmul__(self, lhs):
        return self * lhs
