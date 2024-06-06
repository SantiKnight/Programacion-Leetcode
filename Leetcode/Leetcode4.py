class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        min_len = 100000
        item = ""
        prefix = ""
        
        strs.sort()
        item = strs[0]
        min_len = len(item)
    
        for i in range(min_len):
            for word in strs:
                if word[len(prefix)] == item[len(prefix)]:
                    continue
                else:
                    print(prefix)
                    return prefix
            prefix += item[len(prefix)] if item else ""
        
        return prefix 
s = Solution()
s.longestCommonPrefix([""])