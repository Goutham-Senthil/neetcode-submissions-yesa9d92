class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hastmap = {}

        for i,num in enumerate(nums):
            value = target - num
            if value in hastmap:
                return [hastmap[value],i]
            hastmap[num] = i