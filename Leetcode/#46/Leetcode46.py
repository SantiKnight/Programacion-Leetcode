class Solution:
    def minOperations(self, logs: list[str]) -> int:
        t = 0
        for l in logs:
            l = l.split("/")
            if l[0] == "..":
                if t > 0:
                    t-=1
            elif l[0] != ".":
                t+=1
        return t
            
s = Solution()
s.minOperations(["d1/","d2/","../","d21/","./"])