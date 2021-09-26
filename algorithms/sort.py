# Catalogue of sort algorithms in Python for reference
import random


class Sort:
    def __init__(self, data):
        self.data = data

    ##############################################################
    # Selection Sort
    # Time: O(N^2)
    # Space: O(1)
    ##############################################################
    def selection_sort(self):
        arr = self.data.copy()
        length = len(arr)

        for i in range(length):
            min_index = i
            min_val = arr[i]
            for j in range(i, length):
                if arr[j] < min_val:
                    min_index = j
                    min_val = arr[j]

            arr[min_index] = arr[i]
            arr[i] = min_val

        return arr

    ##############################################################
    # Insertion Sort
    # Time: O(N^2)
    # Space: O(1)
    ##############################################################
    def insertion_sort(self):
        arr = self.data.copy()
        length = len(arr)
        for i in range(1, length):
            val = arr[i]
            j = i - 1
            while j >= 0 and val < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1

            arr[j + 1] = val

        return arr

    ##############################################################
    # Bubble Sort
    # Time: O(N^2)
    # Space: O(1)
    ##############################################################
    def bubble_sort(self):
        arr = self.data.copy()
        valid = False
        length = len(self.data)

        while not valid:
            valid = True
            for i in range(length - 1):
                if arr[i] > arr[i + 1]:
                    valid = False
                    temp = arr[i]
                    arr[i] = arr[i + 1]
                    arr[i + 1] = temp

        return arr

    ##############################################################
    # Merge Sort
    # Time: O(NLog(N))
    # Space: O(N)
    ##############################################################
    def merge_sort(self):
        arr = self.data.copy()

        def merge_sort_recurse(curr_arr):
            if len(curr_arr) <= 1:
                return curr_arr

            mid_index = int(len(curr_arr) / 2)
            left = merge_sort_recurse(curr_arr[:mid_index])
            right = merge_sort_recurse(curr_arr[mid_index:])

            result = []
            i = 0
            j = 0
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1

            while i < len(left):
                result.append(left[i])
                i += 1

            while j < len(right):
                result.append(right[j])
                j += 1

            return result

        arr = merge_sort_recurse(arr)
        return arr

    ##############################################################
    # Quick Sort
    # Time: O(NLog(N))
    # Space: O(N)
    ##############################################################
    def quick_sort(self):
        arr = self.data.copy()

        def quick_sort_recurse(curr_arr):
            if len(curr_arr) <= 1:
                return curr_arr
            rand_index = random.randint(0, len(curr_arr) - 1)
            rand_val = curr_arr[rand_index]
            curr_arr.pop(rand_index)
            left = quick_sort_recurse([num for num in curr_arr if num <= rand_val])
            right = quick_sort_recurse([num for num in curr_arr if num > rand_val])
            new_arr = left
            new_arr.append(rand_val)
            new_arr.extend(right)
            return new_arr

        arr = quick_sort_recurse(arr)
        return arr

    ##############################################################
    # Heap Sort
    # Time: O(NLog(N))
    # Space: O(1)
    ##############################################################
    def heap_sort(self):
        arr = self.data.copy()

        def heapify(curr_arr, curr_index, n):
            largest = curr_index
            left = 2 * curr_index + 1
            right = 2 * curr_index + 2

            if left < n and arr[largest] < arr[left]:
                largest = left

            if right < n and arr[largest] < arr[right]:
                largest = right

            if not largest == curr_index:
                arr[curr_index], arr[largest] = arr[largest], arr[curr_index]
                heapify(curr_arr, largest, n)

        n = len(arr)
        for i in range(n // 2, -1, -1):
            heapify(arr, i, n)

        for i in range(n - 1, 0, -1):
            arr[0], arr[i] = arr[i], arr[0]
            heapify(arr, 0, i)

        return arr

    selection_sort.name = "Selection Sort"
    insertion_sort.name = "Insertion Sort"
    bubble_sort.name = "Bubble Sort"
    merge_sort.name = "Merge Sort"
    quick_sort.name = "Quick Sort"
    heap_sort.name = "Heap Sort"
