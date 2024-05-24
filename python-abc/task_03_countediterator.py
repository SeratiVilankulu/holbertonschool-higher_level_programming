class CountedIterator:
    def __init__(self, iterable):
        self.iterator = iter(iterable)
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        item = next(self.iterator)  # Get the next item from the original iterator
        self.count += 1  # Increment the counter
        return item

    def get_count(self):
        return self.count

