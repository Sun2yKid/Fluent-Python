import abc


class Tombola(abc.ABC):  # 自己定义的抽象基类要继承abc.ABC

    @abc.abstractmethod
    def load(self, iterable):
        """从可迭代对象中添加元素"""

    @abc.abstractmethod
    def pick(self):
        """随机删除元素，然后将其返回
        如果实例为空，这个方法应该抛出‘LookupError’
        """

    def loaded(self):
        """如果至少有一个元素，返回True，否者返回False"""
        return bool(self.inspect())

    def inspect(self):
        """返回一个有序元组，有当前元素构成"""
        items = []
        while True:
            try:
                items.append(self.pick())
            except LookupError:
                break
        self.load(items)
        return tuple(sorted(items))

