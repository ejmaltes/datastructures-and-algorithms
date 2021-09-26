# Catalogue of search algorithms in Python for reference

class Search:
    def __init__(self, data):
        self.data = data

    ##############################################################
    # Linear Search
    # Time: O(N)
    # Space: O(1)
    ##############################################################
    def linear_search(self, target):
        i = 0
        while not self.data[i] == target:
            i += 1
        return i

    ##############################################################
    # Binary Search
    # Time: O(Log(N))
    # Space: O(1)
    ##############################################################
    def binary_search(self, target):
        left = 0
        right = len(self.data)

        while left <= right:
            mid = (left + right) // 2

            if self.data[mid] < target:
                left = mid + 1
            elif self.data[mid] > target:
                right = mid - 1
            elif not left == mid:
                right = mid
            else:
                return mid
        return None

    linear_search.name = "Linear Search"
    binary_search.name = "Binary Search"