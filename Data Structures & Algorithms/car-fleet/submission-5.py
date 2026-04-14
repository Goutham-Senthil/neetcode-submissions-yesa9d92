class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [[p,s] for p,s in zip(position,speed)]
        
        max_time = 0
        fleets = 0

        for p , s in sorted(pairs)[::-1]:
            time = (target-p)/s
            # Condition is to check if the time of the new car(fleet) 
            # is less than(faster) 
            if time > max_time:
                fleets+=1
                max_time = time
        
        return fleets
