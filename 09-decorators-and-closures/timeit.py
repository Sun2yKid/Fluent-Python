"""
inspired by 码农高天
https://www.bilibili.com/video/BV19U4y1d79C/?spm_id_from=pageDriver&vd_source=ea29e3c5e449e8caac08a7cb1368bf11

@dec  只是一个语法糖
    @dec
    def fun(): pass
    等价于:
    fun = dec(fun)
"""
import time

def timeit(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        ret = func(*args, **kwargs)
        print(f"used: {time.time() - start:0.8f}s")
        return ret
    return wrapper


"""
等价于：
    double = timeit(double)
"""
@timeit
def double(x):
    return x * 2

print('*' * 40 + ' 函数装饰器 ')
print(double(2))


def timeit_times(iteration):
    def inner(func):
        def wrapper(*args, **kwargs):
            start = time.time()
            ret = False
            for _ in range(iteration):
                ret = func(*args, **kwargs)
            print(f"run {iteration} times, used: {time.time() - start:0.8f}s")
            return ret

        return wrapper
    return inner


"""
等价于：
    double = timeit_times(10000)(double)
"""
@timeit_times(10000)
def double(x):
    return x * 2

print('*' * 40 + ' 带参数的函数装饰器 ')
print(double(3))



# 装饰器类 1/2
class Timer:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        start = time.time()
        ret = self.func(*args, **kwargs)
        print(f"Time: {time.time() - start:0.8f}s")
        return ret


"""
等价于：
    add = Timer(add)
"""
@Timer
def add(a, b):
    return a + b

print('*' * 40 + ' 装饰器类 1/2 ')
print(add(1, 1))


# 装饰器类 2/2 带参数的`装饰器类`
class TimerWithParam:
    def __init__(self, prefix):
        self.prefix = prefix

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            start = time.time()
            ret = func(*args, **kwargs)
            print(f"{self.prefix}{time.time()-start:0.8f}s")
            return ret
        return wrapper


"""
等价于：
    add = TimerWithParam(prefix="elapsed_time: ")(add)
"""
@TimerWithParam(prefix="elapsed_time: ")
def add(a, b):
    return a + b


print('*' * 40 + ' 装饰器类 2/2 带参数的`装饰器类`')
print(add(1, 2))



# 类装饰器

def add_str(cls):
    def __str__(self):
        return str(self.__dict__)
    cls.__str__ = __str__
    return cls

"""
等价于：
    MyObject = add_str(MyObject)
"""
@add_str
class MyObject:
    def __init__(self, a, b):
        self.a = a
        self.b = b

print('*' * 40 + ' 类装饰器')
o = MyObject(2, 3)
print(o)



"""
把装饰器封装到类里，使得
    * 该装饰器在类里正常使用，
    * 在类外通过对象调用或者类调用都可以正常使用
"""
class Decorators:

    # 可以理解为类的辅助函数，
    def log_function(func):
        def wrapper(*args, **kwargs):
            print(f"func {func.__name__} start")
            print(f"args: {args}")
            ret = func(*args, **kwargs)
            print(f"func end")
            return ret
        return wrapper

    @log_function
    def fib(self, n):
        if n <= 1:
            return 0
        else:
            return self.fib(n - 1) + self.fib(n - 2)

    log_function = staticmethod(log_function)


@Decorators.log_function
def f():
    pass


d = Decorators()


@d.log_function
def g():
    pass


print('*' * 40 + ' 把装饰器封装到类里')

d.fib(3)

f()
g()

