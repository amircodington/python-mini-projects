
class MyRange:
    current = 0

    def __init__(self, start, stop, step):
        self.start = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if MyRange.current < self.stop:
            num = MyRange.current
            MyRange.current += self.step
            return num
        raise StopIteration


for i in MyRange(0, 100, 2):
    print(i)
