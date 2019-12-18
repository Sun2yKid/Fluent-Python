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
