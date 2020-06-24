
class BingoCage:

    def __init__(self, items):
        self._items = list(items)

    def __call__(self, *args, **kwargs):
        return self.pick()

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from empty BingoCage')


