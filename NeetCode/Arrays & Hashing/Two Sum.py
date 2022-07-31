def twoSum(nums: list[int], target: int) -> list[int] | None:
    diff_map = {}
    for i, j in enumerate(nums):
        diff = target - j
        if diff in diff_map:
            return [diff_map[diff], i]
        diff_map[j] = i
    return
