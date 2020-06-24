import keyword
from collections import abc
from example19_2 import load

class FrozenJSON:
    """
    一个只读接口，使用属性表示法访问JSON类对象
    """

    def __init__(self, mapping):
        # # 19-5
        # self.__data = dict(mapping)
        # 19-6
        self.__data = {}
        for key, value in mapping.items():
            if keyword.iskeyword(key):
                key += '_'
            self.__data[key] = value

    def __getattr__(self, name):
        if hasattr(self.__data, name):
            print('in hasattr', name)
            return getattr(self.__data, name)
        else:
            return FrozenJSON.build(self.__data[name])

    @classmethod
    def build(cls, obj):
        if isinstance(obj, abc.Mapping):
            return cls(obj)
        elif isinstance(obj, abc.MutableSequence):
            return [cls.build(item) for item in obj]
        else:
            return obj

print(__name__)

raw_feed = load()
feed = FrozenJSON(raw_feed)
print(len(feed.Schedule.speakers))
print(sorted(feed.Schedule.keys()))
for key, value in sorted(feed.Schedule.items()):
    print('{:3} {}'.format(len(value), key))
