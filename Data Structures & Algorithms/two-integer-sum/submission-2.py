class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i , number in enumerate(nums):
            difference = target-number
            if difference in hashmap:
                return [ hashmap[difference] , i ]
            hashmap[number] = i