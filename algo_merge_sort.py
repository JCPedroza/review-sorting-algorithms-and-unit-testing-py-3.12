"""
This implementation of Merge Sort:
  * Uses recursion.
  * Can be optimized using concurrency.
  * Can be optimized using naturally occurring ordered runs. This would improve the
    best case time complexity to O(n).
  * Could improve auxiliary space complexity to O(1) but the data structure would need
    to change to liked list.

Time Complexity: Best O(n log n) | Avg O(n log n) | Worst O(n log n)
Space Complexity: Total O(n) | Aux O(n)

https://en.wikipedia.org/wiki/merge_sort
https://www.programiz.com/dsa/merge-sort
https://rosettacode.org/wiki/Sorting_algorithms/Merge_sort
"""

from sort_types import IntList, SortingAlgorithm


def merge(left: IntList, right: IntList) -> IntList:
    """Merges two ordered lists into one ordered list."""
    lr_merge = []

    # Loop until left or right is empty
    while left and right:
        # Append the min value of the list first elements to the merged list
        lr_merge.append(left.pop(0) if left[0] <= right[0] else right.pop(0))

    return [*lr_merge, *left, *right]


def merge_sort(nums: IntList) -> IntList:
    """Returns a sorted copy of the input list."""
    if len(nums) < 2:  # Empty and singleton lists are already sorted
        return nums

    mid_idx = len(nums) // 2
    left_nums = nums[:mid_idx]
    righ_nums = nums[mid_idx:]

    return merge(merge_sort(left_nums), merge_sort(righ_nums))


name = "merge sort (recursive)"
algorithm = SortingAlgorithm(merge_sort, name)
