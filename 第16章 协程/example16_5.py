from functools import wraps


def coroutine(func):
    """装饰器：向前执行到第一个`yield`表达式，预激`func`"""
    @wraps(func)
    def primer(*args, **kwargs):
        gen = func(*args, **kwargs)
        next(gen)
        return gen
    return primer


@coroutine
def averager():
    count = 0
    total = 0.0
    average = None
    while True:
        item = yield average
        total += item
        count += 1
        average = total/count


coro_avg = averager()
# next(coro_avg)  # 预激
print(coro_avg.send(10))
print(coro_avg.send(11))
print(coro_avg.send(12))

