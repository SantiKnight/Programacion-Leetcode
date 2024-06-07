class Solution:
    def reverseString(self, s: list[str]) -> None:
        placeholder = ""
        iterator = -1
        n = 0
        for letra in s:
            placeholder = s[iterator]
            s[iterator] = letra
            s[n] = placeholder
            n += 1
            iterator -= 1
            if n >= len(s)//2:
                break
        
s = Solution()
s.reverseString(["A"," ","m","a","n",","," ","a"," ","p","l","a","n",","," ","a"," ","c","a","n","a","l",":"," ","P","a","n","a","m","a"])
        