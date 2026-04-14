class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hashmap = {}
        res = []
        n=len(nums)
        cand1,cand2 = -1 , -1
        c1,c2 = 0,0

        for num in nums:
            if num == cand1:
                c1+=1
            elif num == cand2:
                c2+=1
            else:
                if c1==0:
                    cand1 = cand2
                    c1 = c2
                    cand2 = num
                    c2 =1
                elif c2 == 0:
                    cand2 = num
                    c2 =1
                else:
                    c1-=1
                    c2-=1
        c1,c2= 0,0
        for num in nums:
            if num ==cand1:
                c1+=1
            elif num==cand2:
                c2+=1
        
        if c1>n//3:
            res.append(cand1)
        if c2>n//3:
            res.append(cand2)
            
        return res