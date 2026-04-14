class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        prev = 1
        n = len(nums)

        for i in range(len(nums)):
            if nums[i]<=0 or nums[i]>n:
                nums[i] = n+1
        print(nums)

        for i in range(len(nums)):

        
            val = abs(nums[i])

            # we want to mark this position as negative
            if val>n:
                # do nothing
                pass
            
            else:
                index = val -1
                nums[index] = -1*abs(nums[index])

        print(nums)
        
        for i in range(n):
            if nums[i]>=0:
                return i+1
        
        return n+1