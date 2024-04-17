"""
This implementation of Heap Sort:
  * Uses recursion.

Time Complexity: Best O(n log n) | Avg O(n log n) | Worst O(n log n)
Space Complexity: Total O(n) | Aux O(1)

https://en.wikipedia.org/wiki/heap_sort
https://rosettacode.org/wiki/Sorting_algorithms/Heapsort
https://www.programiz.com/dsa/heap-sort
"""

from sort_types import IntList, Algorithm


def heapify(nums: IntList, heap_size: int, root_idx: int) -> None:
    """Convert target and affected subtrees into a max heap."""
    left_idx = root_idx * 2 + 1
    right_idx = left_idx + 1
    largest_idx = root_idx

    # Check if left child node exists and if it is larger than root node
    if left_idx < heap_size and nums[left_idx] > nums[largest_idx]:
        largest_idx = left_idx

    # Check if right child node exists and if it is larger than current largest node
    if right_idx < heap_size and nums[right_idx] > nums[largest_idx]:
        largest_idx = right_idx

    # If root node is not the largest in the subtree, swap root with largest node and
    # recursively heapify affected child node.
    if root_idx != largest_idx:
        nums[root_idx], nums[largest_idx] = nums[largest_idx], nums[root_idx]
        heapify(nums, heap_size, largest_idx)


def heap_sort(nums: IntList) -> IntList:
    """Sorts the given integer list in ascending order."""
    # Convert list into max heap
    for idx in range(len(nums) // 2 - 1, -1, -1):
        heapify(nums, len(nums), idx)

    # Extract root node (max value) from max heap until heap is empty
    for idx in range(len(nums) - 1, -1, -1):
        nums[0], nums[idx] = nums[idx], nums[0]
        heapify(nums, idx, 0)

    return nums


name = "heap sort (recursive)"
algorithm = Algorithm(heap_sort, name)
