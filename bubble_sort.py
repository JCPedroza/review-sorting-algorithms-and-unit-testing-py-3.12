from sort_types import IntList, SortingAlgorithm


def bubble_sort(nums: IntList) -> IntList:
    swapped = False

    for loop in range(len(nums) - 1):
        for idx in range(len(nums) - loop - 1):
            if nums[idx] > nums[idx + 1]:
                nums[idx], nums[idx + 1] = nums[idx + 1], nums[idx]
                swapped = True

        if not swapped:
            return nums

    return nums


name = "optimized bubble sort"
algorithm = SortingAlgorithm(bubble_sort, name)
