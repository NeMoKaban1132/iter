class MyIterator:
    def __init__(self, iterable):
        self.iterable = iterable
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.iterable):
            raise StopIteration
        value = self.iterable[self.index]
        self.index += 1
        return value
class MyIterable:
    def __init__(self, iterable):
        self.iterable = iterable

    def __iter__(self):
        return MyIterator(self.iterable)
my_list = [1, 2, 3, 4, 5]
my_iterable = MyIterable(my_list)
for item in my_iterable:
    print(item)