class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        
        five = 0
        ten = 0
        twenty = 0

        for i,bill in enumerate(bills):
            if i == 0 and bill!=5:
                return False
            
            # do nothing
            if bill ==5:
                five+=1
            elif bill == 10:
                # we need to give 5
                ten+=1
                if five>0:
                    five-=1
                    continue
                else:
                    return False
            elif bill == 20:
                twenty+=1
                if ten>0 and five>0:
                    five-=1
                    ten-=1
                elif five>=3:
                    five-=3
                else:
                    return False

        return True