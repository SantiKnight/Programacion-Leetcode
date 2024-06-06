class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = list(str(x))
        reversed_x = list(str(x))
        reversed_x = list(reversed_x)
        reversed_x.reverse()
        print(num, reversed_x)
        if num == reversed_x:
            return True
        else:
            return False
                
        
        
s = Solution()
s.isPalindrome(121)