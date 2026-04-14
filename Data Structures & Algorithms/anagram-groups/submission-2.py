class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)

        for j in range(len(strs)):

            chars = [0]*26
            for i in range(len(strs[j])):

                chars[ord(strs[j][i])-ord('a')]+=1
            
            key = tuple(chars)
            hashmap[key].append(strs[j])
        
        return list(hashmap.values())
