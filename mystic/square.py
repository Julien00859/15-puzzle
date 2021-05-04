import random
import itertools


class Square:
    def __init__(self, difficulty):
        for _ in range(difficulty):
            getattr(self, random.choice(list(self.valid_directions())))()

    def _swap(self, z, n):
        self.numbers[n], self.numbers[z] = self.numbers[z], self.numbers[n]

    def valid_directions(self):
        zero_idx = self.numbers.index(0)
        if zero_idx >= 4:
            yield 'up'
        if zero_idx <= 11:
            yield 'down'
        if zero_idx % 4 >= 1:
            yield 'left'
        if zero_idx % 4 <= 1:
            yield 'right'

    def up(self):
        zero_idx = self.numbers.index(0)
        if zero_idx >= 4:
            self._swap(zero_idx, zero_idx - 4)

    def down(self):
        zero_idx = self.numbers.index(0)
        if zero_idx <= 11:
            self._swap(zero_idx, zero_idx + 4)

    def left(self):
        zero_idx = self.numbers.index(0)
        if zero_idx % 4 >= 1:
            self._swap(zero_idx, zero_idx - 1)

    def right(self):
        zero_idx = self.numbers.index(0)
        if zero_idx % 4 <= 1:
            self._swap(zero_idx, zero_idx + 1)

    def is_won(self):
        return self.count_valid() == 16

    def count_valid(self):
        count = 0
        for idx, n in enumerate(self.numbers):
            if idx == n:
                count += 1
        return count


