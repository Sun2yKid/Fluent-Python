"""
inspired by 码农高天
https://www.bilibili.com/video/BV13F411g7CD/?spm_id_from=pageDriver&vd_source=ea29e3c5e449e8caac08a7cb1368bf11

metaclass就是让你可以更灵活的掌握建立类中间的逻辑
"""
import random

class M(type):
    def __new__(cls, name, base, dict):
        """
        class被定义时调用
        """
        print("__new__", name, base, dict)
        # return type.__new__(cls, name, base, dict)
        return super().__new__(cls, name, base, dict)   # Note: 有参数cls

    def __init__(self, name, base, dict):
        """
        class被定义时调用，在__new__之后，区别：已经有A2这个object了，并没有创建
        """
        print("__init__", name, base, dict)
        self.random_id = random.randint(0, 100)
        # return type.__init__(self, name, base, dict)
        return super().__init__(name, base, dict)       # Note: 没有有参数self

    def __call__(cls, *args, **kwargs):
        """
        不是在class被定义时调用，而是class在产生实例时被调用
        """
        print("__call__")
        # return type.__call__(cls, *args, **kwargs)
        return super().__call__(*args, **kwargs)        # Note: 没有有参数cls

# 等价于 type("A", (), {})
class A:
    pass

# 用M返回需要的类，不要用type建立class了，用M建立class
# 等价于 A2 = M("A2", (), {})
class A2(metaclass=M):
    pass


# 实际上调用A的__new__函数，和__init__函数
o = A()

# 实际上调用M的__new__函数，和__init__函数
o2 = A2()    # A2 () {'__module__': '__main__', '__qualname__': 'A2'}
print(o2.random_id)
