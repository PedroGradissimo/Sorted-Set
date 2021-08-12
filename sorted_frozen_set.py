class SortedFrozenSet:

    def __init__(self, item=None):
        self._items = (
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