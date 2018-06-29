import random


# a generator that yields items instead of returning a list
def firstn(n):
    num = 0
    while num < n:
        yield num
        num += 1


sum_of_first_n = sum(firstn(1000000))
a = firstn(10000)
# print(a)


class RandomIterable:
    def __init__(self):
        self.val = 0

    def __iter__(self):
        return self

    def __next__(self):
        # if random.choice(["go", "go", "stop"]) == "stop":
        #    raise StopIteration  # signals "the end"
        if self.val == 100:
            raise StopIteration
        self.val += 1
        return self.val


# print(list(RandomIterable()))
# print(list(RandomIterable()))
a = iter(RandomIterable())
b = RandomIterable()
print(a)
print(next(a))
print(next(a))

for i in a:
    print(i)
