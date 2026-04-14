class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(t) > len(s) or t =="":
            return ""

        t_dict = Counter(t)

        window = {}

        have , need = 0 , len(t_dict)

        result , reslen = [-1,-1] , float("infinity")
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c,0) 

            if c in t_dict and window[c] == t_dict[c]:
                have+=1
            
            while have == need:

                if (r-l+1) < reslen:
                    result = [l,r]
                    reslen = (r-l+1)

                window[s[l]] -=1
                if s[l] in t_dict and window[s[l]] < t_dict[s[l]]:
                    have -=1
                l+=1
        
        l , r  = result

        return s[l:r+1] if reslen != float("infinity") else ""