import time
import functools


# Timer decorator
def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"Runtime for {args[0].num_tests} tests of length {args[0].length}: {end - start} seconds")
        return result
    return wrapper
