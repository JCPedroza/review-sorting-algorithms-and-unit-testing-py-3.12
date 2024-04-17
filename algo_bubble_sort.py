"""
This implementation of Bubble Sort:
  * Uses a boolean flag to improve the best case time complexity from O(n^2)to O(n) by
    terminating early if the list is already sorted.
  * Avoids processing the sorted portion of the list by having len(nums) - loop - 1 as
    the stop of the inner loop range.

Time Complexity: Best O(n) | Avg O(n^2) | Worst O(n^2)
Space Complexity: Total O(n) | Aux O(1)

https://en.wikipedia.org/wiki/bubble_sort
https://rosettacode.org/wiki/Sorting_algorithms/Bubble_sort
https://www.programiz.com/dsa/bubble-sort
"""

from sort_types import IntList, Algorithm


def bubble_sort(nums: IntList) -> IntList:
    """Sorts the given integer list in ascending order."""
    for loop in range(len(nums) - 1):
        is_sorted = True

        # Loop through the unsorted portion and swap unsorted adjacent pairs
        for idx in range(len(nums) - loop - 1):
            if nums[idx] > nums[idx + 1]:
                nums[idx], nums[idx + 1] = nums[idx + 1], nums[idx]
                is_sorted = False  # Don't terminate early

        if is_sorted:
            return nums  # Terminate early

    return nums


name = "bubble sort (optimized)"
algorithm = Algorithm(bubble_sort, name)
