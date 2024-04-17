"""
This implementation of Selection Sort:
  * Avoids processing the sorted portion of the list by having loop + 1 as the start of
    the inner loop range.
  * Avoids boolean flag for early termination optimization since it only works for
    lists that are already initially sorted, and not for lists that are sorted during
    the process, so the overhead is avoided.

Time Complexity: Best O(n^2) | Avg O(n^2) | Worst O(n^2)
Space Complexity: Total O(n) | Aux O(1)

https://en.wikipedia.org/wiki/selection_sort
https://www.programiz.com/dsa/selection-sort
https://rosettacode.org/wiki/Sorting_algorithms/Selection_sort
"""

from sort_types import IntList, Algorithm


def selection_sort(nums: IntList) -> IntList:
    """Sorts the given integer list in ascending order."""
    for loop in range(len(nums)):
        min_val_idx = loop

        # Loop through the unsorted portion and find the min value
        for idx in range(loop + 1, len(nums)):
            if nums[idx] < nums[min_val_idx]:
                min_val_idx = idx

        # Move min value of unsorted portion to the new end of the sorted portion
        nums[loop], nums[min_val_idx] = nums[min_val_idx], nums[loop]

    return nums


name = "selection sort (no early termination)"
algorithm = Algorithm(selection_sort, name)
