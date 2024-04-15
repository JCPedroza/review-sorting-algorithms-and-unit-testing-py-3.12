def bubble_sort(nums: list[int]) -> list[int]:
    swapped = False

    for loop in range(len(nums) - 1):
        for idx in range(len(nums) - loop - 1):
            if nums[idx] > nums[idx + 1]:
                nums[idx], nums[idx + 1] = nums[idx + 1], nums[idx]
                swapped = True

        if not swapped:
            return nums

    return nums
