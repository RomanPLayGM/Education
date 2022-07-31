# Search Rotated Sorted Array
class Solution(object):
    def search(self, nums, target):
        """
        type nums: List[int]
        :param nums:
        :type target: int
        :rtype: int
        """
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid
            # Сравниваем с левым краем
            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                # Сравниваем с правым краем
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1


# if len(nums) == 0:
#             return -1
#         left = 0
#         right = len(nums)-1
#         while left < right:
#             mid = (left + right)/2
#             if nums[mid] > nums[right]:
#                 left = mid + 1
#             else:
#                 right = mid
#         start = left
#         left = 0
#         right = len(nums)-1
#         if target >= nums[start] and target <= nums[right]:
#             left = start
#         else:
#             right = start
#         while left <= right:
#             mid = (left + right)/2
#             if nums[mid]==target:
#                 return mid
#             elif nums[mid] <= target:
#                 left = mid + 1
#             else:
#                 right = mid - 1
#         return -1
