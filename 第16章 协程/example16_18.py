"""
委派生成器中
RESULT = yield from EXPR
简化的伪代码：不支持.throw()和.close()方法，而且只处理StopIteration异常
"""

"""
_i =iter(EXPR)
try:
    _y = next(_i)
except StopIteration as _e:
    _r = _e.value
else:
    while 1:
        _s = yield _y
        try:
            _y = _i.send(_s)
        except StopIteration as _e:
            _r = _e.value
            break

RESULT = _r
"""
