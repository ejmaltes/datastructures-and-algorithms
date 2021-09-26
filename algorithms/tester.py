import random
from algorithms.sort import Sort
from algorithms.decorators import timer


class Tester:
    def __init__(self, num_tests=100, length=100, min_val=-100, max_val=100):
        self.rands = []
        self.sorts = []
        self.num_tests = num_tests
        self.length = length
        self.min_val = min_val
        self.max_val = max_val
        self.set_table()

    def get_sample(self):
        sample = []
        for i in range(self.length):
            sample.append(random.randint(self.min_val, self.max_val))
        return sample

    def set_table(self):
        for i in range(self.num_tests):
            rand_arr = self.get_sample()
            sorted_arr = sorted(rand_arr)
            self.rands.append(rand_arr)
            self.sorts.append(sorted_arr)

    @timer
    def test(self, obj, func, search=False, is_sorted=False):
        if search:
            num_err = 0
            if is_sorted:
                for arr in self.sorts:
                    rand_val = random.choice(arr)
                    rand_index = arr.index(rand_val)
                    obj.data = arr
                    evaluated_index = func(rand_val)

                    if not rand_index == evaluated_index:
                        print(rand_index, evaluated_index, arr)
                        num_err += 1
            else:
                for arr in self.rands:
                    rand_val = random.choice(arr)
                    rand_index = arr.index(rand_val)
                    obj.data = arr
                    if not rand_index == func(rand_val):
                        num_err += 1
            return num_err
        else:
            result = []
            for arr in self.rands:
                obj.data = arr
                result.append(func())

            return self.compare_arr(result)

    def compare_arr(self, compare_to):
        num_err = 0
        for i in range(len(self.sorts)):
            if not self.sorts[i] == compare_to[i]:
                print(f"Error: Mismatch \\ {self.sorts[i]} \\ {compare_to[i]}")
                num_err += 1
        return num_err
