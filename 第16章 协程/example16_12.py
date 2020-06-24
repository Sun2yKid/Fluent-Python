class DemoException(Exception):
    """为这次演示定义的异常类型"""


def demo_exc_handling():
    print('-> coroutine started')
    try:
        while True:
            try:
                x = yield
            except DemoException:
                print('*** DemoException handled. Continuing...')
            else:
                print('-> coroutine received: {!r}'.format(x))
    finally:
        print('-> coroutine ending')

from inspect import getgeneratorstate

exc_coro = demo_exc_handling()
print(getgeneratorstate(exc_coro))
next(exc_coro)
print(getgeneratorstate(exc_coro))
print(exc_coro.send(11))
print(getgeneratorstate(exc_coro))
print(exc_coro.send(22))

print('*' * 10, 'throw DemoException', '*' * 10)
exc_coro.throw(DemoException)
print(getgeneratorstate(exc_coro))

print('*' * 10, 'throw ZeroDivisionError', '*' * 10)
exc_coro.throw(ZeroDivisionError)
print(getgeneratorstate(exc_coro))

exc_coro.close()
print(getgeneratorstate(exc_coro))


