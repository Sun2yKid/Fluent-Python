from random import randrange

from .example11_9 import Tombola


@Tombola.register
class TomoList(list):  # list的真实子类，Tombola的虚拟子类

    def pick(self):
        if self:
            position = randrange(len(self))
            return self.pop(position)
        else:
            raise LookupError('pop from empty TomoList')

    load = list.extend

    def loaded(self):
        return bool(self)

    def inspect(self):
        return tuple(sorted(self))


# Tombola.register(TomoList)
