# import itertools
#
#
# def permutations(string):
#     print(len(set("".join(p) for p in set(itertools.permutations(string)))))
#     return list("".join(p) for p in set(itertools.permutations(string)))
#
# Задача-Contains_Duplicate:
# print(permutations("dgfhfhgfhrf"))
# class Solution:
#     def containsDuplicate(self, nums) -> bool:
#         nums_1 = list(set(nums))
#         if len(nums_1) == len(nums):
#             return False
#         return True
#
#
# print(Solution().containsDuplicate([3, 1]))
# Задача - Two_Sum:
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         diff_map = {}
#         for i, j in enumerate(nums):
#             diff = target - j
#             if diff in diff_map:
#                 return [diff_map[diff], i]
#             diff_map[j] = i
#         return
# Бинарный поиск
# class Solution:
#    def search(self, nums, target: int) -> int:
#        low, high = 0, len(nums) - 1
#        while low <= high:
#            mid = (low + high) // 2
#            guess = nums[mid]
#            if guess == target:
#                return mid
#            if guess > target:
#                high = mid - 1
#            else:
#                low = mid + 1
#        return -1
#
#
# a = Solution()
# print(a.search([-1, 0, 3, 5, 9, 12], 9))

# Сложность O(N * log(M))
class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
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


a = Solution()
print(a.searchMatrix([[1]], 1))

# O(log(M) + log(N)) - сложность


class Solution(object):

    def searchMatrix(self, matrix, target):
        ROWS, COLS = len(matrix), len(matrix[0])
        top, bot = 0, ROWS - 1
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
        l, r = 0, COLS - 1
        while l <= r:
            m = (l + r) // 2
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else:
                return True
        return False


a = Solution()
print(a.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3))
