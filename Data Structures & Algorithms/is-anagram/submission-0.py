from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False

        s_dict = Counter(s)
        t_dict = Counter(t)


        for key,value in s_dict.items():
            if key not in t_dict:
                return False
            elif value!=t_dict[key]:
                return False

        return True