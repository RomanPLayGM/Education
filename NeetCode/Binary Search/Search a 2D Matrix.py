# Сложность O(N * log(M))

def searchMatrix(matrix: list[list[int]], target: int) -> bool:
    def search(nums, target_0):
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            guess = nums[mid]
            if guess == target_0:
                return True
            if guess > target_0:
                high = mid - 1
            else:
                low = mid + 1
        return False

    if len(matrix) > 1:
        if target < matrix[0][0]:
            return False
        if target > matrix[-1][-1]:
            return False
        for i in range(0, len(matrix) - 1):
            line = matrix[i]
            next_line = matrix[i + 1]
            if line[0] <= target < next_line[0]:
                return search(line, target)
            elif target == next_line[0]:
                return True
            elif next_line[0] <= target <= next_line[-1]:
                return search(next_line, target)
    else:
        return search(matrix[0], target)


print(searchMatrix([[1]], 1))


# O(log(M) + log(N)) - сложность


def searchMatrix(matrix, target):
    rows, cols = len(matrix), len(matrix[0])
    top, bot = 0, rows - 1
    while top <= bot:
        row = (top + bot) // 2
        if target > matrix[row][-1]:
            top = row + 1
        elif target < matrix[row][0]:
            bot = row - 1
        else:
            break
    if not (top <= bot):
        return False
    row = (top + bot) // 2
    left, right = 0, cols - 1
    while left <= right:
        m = (left + right) // 2
        if target > matrix[row][m]:
            left = m + 1
        elif target < matrix[row][m]:
            right = m - 1
        else:
            return True
    return False


print(searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3))
