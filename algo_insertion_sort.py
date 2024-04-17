"""
This implementation of Insertion Sort:
  * Has built-in early termination optimization.
  * Could be optimized by reducing the number of swaps and comparisons, but this
    version is used to preserve logic simplicity.

Time Complexity: Best O(n) | Avg O(n^2) | Worst O(n^2)
Space Complexity: Total O(n) | Aux O(1)

https://en.wikipedia.org/wiki/insertion_sort
https://www.programiz.com/dsa/insertion-sort
https://rosettacode.org/wiki/Sorting_algorithms/Insertion_sort
"""

from sort_types import IntList, Algorithm


def insertion_sort(nums: IntList) -> IntList:
    """Sorts the given integer list in ascending order."""
    for loop in range(1, len(nums)):
        idx = loop

        # Swap left until the correct place inside the sorted portion is found
        while nums[idx - 1] > nums[idx] and idx > 0:
            nums[idx - 1], nums[idx] = nums[idx], nums[idx - 1]
            idx -= 1

    return nums


name = "insertion sort (naive)"
algorithm = Algorithm(insertion_sort, name)
