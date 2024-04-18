"""
This implementation of Quick Sort:
  * Uses recursion.
  * Is stable, but at the cost of O(n) space complexity.
  * Could be optimized by choosing a pivot at random.

Time Complexity: Best O(n log n) | Avg O(n log n) | Worst O(n^2)
Space Complexity: Total O(n) | Aux O(n)

https://en.wikipedia.org/wiki/quick_sort
https://rosettacode.org/wiki/Sorting_algorithms/Quicksort
https://www.programiz.com/dsa/quick-sort
"""

from sort_types import IntList, Algorithm


def quick_sort(nums: IntList) -> IntList:
    """Returns a sorted copy of the input list in ascending order."""
    if len(nums) < 2:  # Empty and singleton lists are already sorted
        return nums

    pivot_val = nums[0]
    left_nums: IntList = []
    right_nums: IntList = []

    # Partition based on pivot's value
    for num in nums[1:]:
        if num < pivot_val:
            left_nums.append(num)
        else:
            right_nums.append(num)

    # Recursively sort sublists and combine results
    return [*quick_sort(left_nums), pivot_val, *quick_sort(right_nums)]


name = "quick sort"
algorithm = Algorithm(quick_sort, name)
