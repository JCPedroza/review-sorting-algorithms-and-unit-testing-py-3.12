"""
This implementation of Selection Sort uses a boolean flag to improve the best case time
complexity from O(n^2)to O(n) by terminating early if the list is already sorted.

Time Complexity: Best O(n) | Avg O(n^2) | Worst O(n^2)
Space Complexity: Total O(n) | Aux O(1)

https://en.wikipedia.org/wiki/Bubble_sort
https://www.programiz.com/dsa/bubble-sort
https://rosettacode.org/wiki/Sorting_algorithms/Bubble_sort
"""

from sort_types import IntList, SortingAlgorithm


def selection_sort(nums: IntList) -> IntList:
    """Sorts the given integer list in ascending order."""
    for loop in range(len(nums)):
        is_ordered = True
        min_val_idx = loop

        # Loop through the unsorted portion of the list and find the min value
        for idx in range(loop + 1, len(nums)):
            if nums[idx] < nums[min_val_idx]:
                min_val_idx = idx
                is_ordered = False  # Don't terminate early

        if is_ordered:
            return nums  # Terminate early

        # Move min value of unsorted portion to the new end of the sorted portion
        nums[loop], nums[min_val_idx] = nums[min_val_idx], nums[loop]

    return nums


name = "selection sort (optimized best case)"
algorithm = SortingAlgorithm(selection_sort, name)
