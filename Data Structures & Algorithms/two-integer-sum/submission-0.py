class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map_seen = {}
        for i,element in enumerate(nums):
            required = target-element
            if required in map_seen:
                return [map_seen[required],i]
            map_seen[element]=i
