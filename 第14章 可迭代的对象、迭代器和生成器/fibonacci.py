# 1. 使用生成器生成斐波那契数列
import heapq
import numbers


def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


print(fibonacci, type(fibonacci))
f = fibonacci()
print(f, type(f))

for i in range(6):
    print(next(f))

print('=============================================================')
# 2. 使用递归+缓存
import functools


@functools.lru_cache()
def fibonacci_1(n):
    if n < 2:
        return n
    return fibonacci_1(n-2) + fibonacci_1(n-1)

print('fibonacci_1', fibonacci_1(6))


print('=============================================================')
# 3. 使用循环

def fibonacci_2(n):
    a, b = 0, 1
    while n > 0 and isinstance(n, numbers.Integral):
        a, b = b, a + b
        n -= 1

    return a

print('fibonacci_2', fibonacci_2(6))

print('=============================================================')
