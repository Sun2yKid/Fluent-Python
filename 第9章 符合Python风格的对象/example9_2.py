import math
from array import array


class Vector2d:
    __slots__ = ('__x', '__y', '__dict__')

    typecode = 'd'

    def __init__(self, x, y):
        self.__x = float(x)
        self.__y = float(y)

    def __iter__(self):
        return (i for i in (self.x, self.y))

    def __repr__(self):
        class_name = type(self).__name__
        return '{}({!r}, {!r})'.format(class_name, *self)

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) +
                bytes(array(self.typecode, self)))

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    # 9-3
    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(*memv)

    # 9-5
    # def __format__(self, fmt_spec=''):
    #     components = (format(c, fmt_spec) for c in self)
    #     return '({}, {})'.format(*components)

    # 9-6
    def __format__(self, fmt_spec=''):
        if fmt_spec.endswith('p'):
            fmt_spec = fmt_spec[:-1]
            coords = (abs(self), self.angle())
            outer_fmt = '<{}, {}>'
        else:
            coords = self
            outer_fmt = '({}, {})'
        components = (format(c, fmt_spec) for c in coords)
        return outer_fmt.format(*components)

    def angle(self):
        return math.atan2(self.y, self.x)

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def __hash__(self):
        return hash(self.x) ^ hash(self.y)


# 9-10
v1 = Vector2d(3, 4)
print(v1.__dict__)
print(v1._Vector2d__y)

# 9-13
v2 = Vector2d(1.1, 2.2)
dumpd = bytes(v2)
print(dumpd, len(dumpd), v2.typecode)
v2.typecode = 'f'
dumpf = bytes(v2)
print(dumpf, len(dumpf), v2.typecode, Vector2d.typecode)


# 9-14
class ShortVector2d(Vector2d):
    typecode = 'f'


sv = ShortVector2d(1/11, 1/27)
print(sv, len(bytes(sv)), sv.typecode)
