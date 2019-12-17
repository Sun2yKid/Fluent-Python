"""
Size类的源码，位于python3\Lib\_collections_abc.py
"""
import abc


class Sized(metaclass=abc.ABCMeta):

    __slots__ = ()

    @abc.abstractmethod
    def __len__(self):
        return 0

    @classmethod
    def __subclasshook__(cls, C):
        if cls is Sized:
            if any("__len__" in B.__dict__ for B in C.__mro__):
                return True
        return NotImplemented
