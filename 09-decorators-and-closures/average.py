# class-based implementation
class Averager:

    def __init__(self):
        self.series = []

    def __call__(self, new_value):
        self.series.append(new_value)
        return sum(self.series) / len(self.series)


# functional implementation
def make_averager():
    series = []

    def averager(new_value):
        series.append(new_value)
        return sum(series) / len(series)

    return averager


def make_averager2():
    count = 0
    total = 0

    def averager(new_value):
        nonlocal count, total
        count += 1
        total += new_value
        return total / count
    return averager


if __name__ == "__main__":

    print(make_averager.__code__)  # <code object make_averager at 0x7fe54250d9d0, file "/Users/zhonghui.yao/OneDrive/Git/Fluent Python/09-decorators-and-closures/average.py", line 13>
    print(f"make_averager.__code__.co_nlocals: {make_averager.__code__.co_nlocals}")    # 1

    print(f"make_averager.__code__.co_varnames: {make_averager.__code__.co_varnames}")  # ('averager',)
    print(f"make_averager.__code__.co_names: {make_averager.__code__.co_names}")  # ()
    print(f"make_averager.__code__.co_cellvars: {make_averager.__code__.co_cellvars}")  # ('series',)
    print(f"make_averager.__code__.co_freevars: {make_averager.__code__.co_freevars}")  # ()

    print(f"make_averager.__code__.co_consts: {make_averager.__code__.co_consts}")  # (None, <code object averager at 0x7fe54250d920, file "/Users/zhonghui.yao/OneDrive/Git/Fluent Python/09-decorators-and-closures/average.py", line 16>, 'make_averager.<locals>.averager')

    avg = make_averager()
    print(avg(10))
    print(avg(11))
    print(avg(12))

    print(avg.__code__)   # <code object averager at 0x7fc86e50d920, file "/Users/zhonghui.yao/OneDrive/Git/Fluent Python/09-decorators-and-closures/average.py", line 16>
    print(f"avg.__code__.co_nlocals: {avg.__code__.co_nlocals}")    # 1

    print(f"avg.__code__.co_varnames: {avg.__code__.co_varnames}")   # ('new_value',)
    print(f"avg.__code__.co_names: {avg.__code__.co_names}")   # ('append', 'sum', 'len')
    print(f"avg.__code__.co_cellvars: {avg.__code__.co_cellvars}")   # ()
    print(f"avg.__code__.co_freevars: {avg.__code__.co_freevars}")     # ('series',)

    print(f"avg.__code__.co_consts: {avg.__code__.co_consts}")     # ('series',)

    print(avg.__closure__)  # (<cell at 0x7fc790192e20: list object at 0x7fc79018d600>,)
    print(avg.__closure__[0].cell_contents)  # [10, 11, 12]





