from sort_types import IntList, SortingAlgorithm


def bubble_sort(nums: IntList) -> IntList:
    """Sorts the given integer list in ascending order."""
    is_sorted = True

    for loop in range(len(nums) - 1):
        for idx in range(len(nums) - loop - 1):
            if nums[idx] > nums[idx + 1]:
                nums[idx], nums[idx + 1] = nums[idx + 1], nums[idx]
                is_sorted = False

        if is_sorted:
            return nums

    return nums


name = "optimized bubble sort"
algorithm = SortingAlgorithm(bubble_sort, name)
