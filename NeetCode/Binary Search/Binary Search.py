# Бинарный поиск
def search(nums, target: int) -> int:
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = nums[mid]
        if guess == target:
            return mid
        if guess > target:
            high = mid - 1
        else:
            low = mid + 1
    return -1


print(search([-1, 0, 3, 5, 9, 12], 9))
