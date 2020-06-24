import functools

registry = set()


def register(active=True):
    def decorate(func):
        print('running register(active=%s)->decorate(%s)' % (active, func))
        if active:
            registry.add(func)
        else:
            registry.discard(func)
        return func
    return decorate


@register(active=False)
def f1():
    print('running f1()')


@register()
def f2():
    print('running f2()')


def f3():
    print('running f3()')


print('registry: ', registry)
# 将f3添加进registry
register()(f3)
print('registry: ', registry)
# 将f2从registry中删除
register(active=False)(f2)
print('registry: ', registry)
