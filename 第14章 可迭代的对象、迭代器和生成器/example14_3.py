"""
Iterator类的源码，位于python3\Lib\_collections_abc.py
"""
import abc


### ONE-TRICK PONIES ###

def _check_methods(C, *methods):
    mro = C.__mro__
    for method in methods:
        for B in mro:
            if method in B.__dict__:
                if B.__dict__[method] is None:
                    return NotImplemented
                break
        else:
            return NotImplemented
    return True


class Iterable(metaclass=abc.ABCMeta):

    __slots__ = ()

    @abc.abstractmethod
    def __iter__(self):
        while False:
            return None

    @classmethod
    def __subclasshook__(cls, C):
        if cls is Iterable:
            return _check_methods(C, '__iter__')
        return NotImplemented


class Iterator(Iterable):

    __slots__ = ()

    @abc.abstractmethod
    def __next__(self):
        'Return the next item from the iterator. When exhausted, raise StopIteration'
        raise StopIteration

    def __iter__(self):
        return self

    @classmethod
    def __subclasshook__(cls, C):
        if cls is Iterator:
            return _check_methods(C, '__iter__', '__next__')
        return NotImplemented

