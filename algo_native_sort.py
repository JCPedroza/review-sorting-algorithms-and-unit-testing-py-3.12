from sort_types import Algorithm, IntList


def native_sort(nums: IntList) -> IntList:
    """Sorts the given integer list in ascending order."""
    nums.sort()
    return nums


name = "native sort (python)"
algorithm = Algorithm(native_sort, name)
