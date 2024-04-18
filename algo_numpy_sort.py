"""
This is a wrapper for Numpy's sorting algorithm.
"""

from numpy import sort
from sort_types import Algorithm, IntList


def numpy_sort(nums: IntList) -> IntList:
    """Returns a sorted copy of the input list in ascending order."""
    return sort(nums)


name = "numpy sort"
algorithm = Algorithm(numpy_sort, name)
