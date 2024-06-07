class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        left = 0
        ans = 0
        ventana = 0
        
        for der in range(len(s)):
            ventana += abs(ord(s[der])-ord(t[der]))
            
            if ventana > maxCost:
                ventana -= abs(ord(s[left])-ord(t[left]))
                left += 1
            
            ans = max(ans, der - left + 1)
        
s = Solution()
s.equalSubstring(s = "krrgw", t = "zjxss", maxCost = 19)