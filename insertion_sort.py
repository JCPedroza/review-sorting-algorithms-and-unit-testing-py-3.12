from sort_types import IntList, SortingAlgorithm


def insertion_sort(nums: IntList) -> IntList:
    """Sorts the given integer list in ascending order."""
    for loop in range(1, len(nums)):
        idx = loop

        while nums[idx - 1] > nums[idx] and idx > 0:
            nums[idx - 1], nums[idx] = nums[idx], nums[idx - 1]
            idx -= 1

    return nums


name = "naive insertion sort"
algorithm = SortingAlgorithm(insertion_sort, name)
