class Solution:
    def minDays(self, bloomDay: list[int], m: int, k: int) -> int:
        n=len(bloomDay)
        if m*k>n: 
            return -1

        def f(d):
            l, bouquet=0, 0
            i=0
            while i<n:
                while i<n and bloomDay[i]<=d:
                    l+=1
                    if l==k:
                        bouquet+=1
                        l=0
                    i+=1
                if i<n and bloomDay[i]>d: l=0
                if bouquet>m: return True
                i+=1
            return bouquet>=m

        l, r = min(bloomDay), max(bloomDay)
        while l < r:
            mid = l + (r - l) // 2
            if f(mid):
                r = mid
            else:
                l = mid + 1
        return l
s = Solution()
s.minDays([1,10,3,10,2], 3, 1)