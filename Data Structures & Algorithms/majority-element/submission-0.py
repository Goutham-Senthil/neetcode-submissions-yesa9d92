class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        candidate = nums[0]
        cand_count = 1
        
        for num in nums[1:]:
            if num!=candidate:
                cand_count-=1
            else:
                cand_count+=1
            
            if cand_count==0:
                cand_count=1
                candidate=num
        
        return candidate