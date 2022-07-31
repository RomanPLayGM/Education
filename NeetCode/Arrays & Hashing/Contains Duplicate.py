#  Задача-Contains_Duplicate:
def containsDuplicate(nums) -> bool:
    hashset = set()
    for n in nums:
        if n in hashset:
            return True
        hashset.add(n)
    return False

