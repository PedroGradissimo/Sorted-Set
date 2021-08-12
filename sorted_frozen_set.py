class SortedFrozenSet:

    def __init__(self, item=None):
        self._items = (
            list(item) if (item is not None)
            else list()
        )

    # This special method accepts a single argument which is the item
    # for which to test for containment, and returns a boolean
    def __contains__(self, item):
        return item in self._items
