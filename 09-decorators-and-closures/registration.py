"""
function decorators are executed as soon as the module is loaded
"""
registry = []


def register(func):
    print(f"running register({func})")
    registry.append(func)
    return func


@register
def f1():
    print('running f1()')


@register
def f2():
    print('running f2()')


def f3():
    print('running f3()')


def main():
    print('running main()')
    print(f"registry: {registry}")
    f1()
    f2()
    f3()
    print(f"registry: {registry}")


if __name__ == '__main__':
    main()

