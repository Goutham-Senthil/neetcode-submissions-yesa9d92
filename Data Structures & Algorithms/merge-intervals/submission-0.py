class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort()
        
        result = [intervals[0]]

        for start,end in intervals:
            prev_end = result[-1][1]

            if start<=prev_end:
                result[-1][0] = min(result[-1][0],start)
                result[-1][1] = max(prev_end,end)
            else:
                result.append([start,end])
        
        return result