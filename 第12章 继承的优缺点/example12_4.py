class A:
    def ping(self):
        print('ping:', self)


class B(A):
    def pong(self):
        print('pong:', self)


class C(A):
    def pong(self):
        print('PONG:', self)


class D(B, C):

    def ping(self):
        super().ping()
        print('post-ping:', self)

    def pingpong(self):
        self.ping()
        super().pong()
        self.pong()
        super().pong()
        C.pong(self)


# 12-8
def print_mro(cls):  # MRO: Method Resolution Order 方法解析顺序
    print(', '.join(c.__name__ for c in cls.__mro__))


print(bool.__mro__)
print_mro(bool)
