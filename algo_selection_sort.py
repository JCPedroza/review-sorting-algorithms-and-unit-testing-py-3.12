from sort_types import IntList, SortingAlgorithm


def selection_sort(nums: IntList) -> IntList:
    """Sorts the given integer list in ascending order."""
    for loop in range(len(nums)):
        min_val_idx = loop

        for idx in range(loop + 1, len(nums)):
            if nums[idx] < nums[min_val_idx]:
                min_val_idx = idx

        nums[loop], nums[min_val_idx] = nums[min_val_idx], nums[loop]

    return nums


name = "selection sort"
algorithm = SortingAlgorithm(selection_sort, name)
