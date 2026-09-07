# Day 4: Instance Methods and Object State
# Q3 - Counter Class

class Counter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

    def decrement(self):
        self.count -= 1

    def reset(self):
        self.count = 0

    def get_count(self):
        return self.count

# Test
c = Counter()
c.increment()
c.increment()
c.increment()
c.decrement()
print(c.get_count())
c.reset()
print(c.get_count())