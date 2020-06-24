from collections import namedtuple


Result = namedtuple('Result', 'count average')


def averager():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield
        if term is None:
            break
        total += term
        count += 1
        average = total/count
    return Result(count, average)


coro_avg = averager()
next(coro_avg)
print(coro_avg.send(10))
print(coro_avg.send(11))
print(coro_avg.send(12))
# # 16-14
# print(coro_avg.send(None))
# 16-15
try:
    coro_avg.send(None)
except StopIteration as exc:
    result = exc.value
    print(result)
