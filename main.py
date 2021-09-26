from algorithms.sort import Sort
from algorithms.search import Search
from algorithms.tester import Tester

searcher = Search([])
# sorter = Sort([])
# funcs = [sorter.selection_sort, sorter.insertion_sort, sorter.bubble_sort, sorter.merge_sort, sorter.quick_sort, sorter.heap_sort]
funcs = [searcher.linear_search, searcher.binary_search]
is_sorted = [searcher.binary_search]
tester = Tester(length=1000)
for func in funcs:
    print(f"Running {func.name}:")
    if func in is_sorted:
        num_errors = tester.test(searcher, func, search=True, is_sorted=True)
    else:
        num_errors = tester.test(searcher, func, search=True)
    print(f"Total Errors: {num_errors} \n")
