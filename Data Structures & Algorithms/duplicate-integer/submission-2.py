# class Solution:
#     def hasDuplicate(self, nums: List[int]) -> bool:
#         for i,element in enumerate(nums):
#             for j in range(i+1,len(nums)):
#                 if element == nums[j]:
#                     return True
#         return False
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                    return True
        else:
            return False