class SortedFrozenSet:

    def __init__(self, item=None):
        self._items = sorted(
            set(item) if (item is not None)
            else set()
        )

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
                repr(self._items)
                if self._items else ""
            )
        )