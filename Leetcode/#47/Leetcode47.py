class Solution:
    def reverseParentheses(self, s: str) -> str:
        s = list(s)
        bolean = False
        a = 0
        b = 0
        while "(" in s:
            t = s.count("(")
            texto = []
            for i in range(len(s)):
                if s[i] == "(":
                    t -= 1
                    if t == 0:
                        bolean= True
                        a = i
                elif bolean:
                    if s[i] == ")":
                        bolean = False
                        b = i
                        for j in range(len(texto)-1,-1,-1):
                            s[i-j-1] = texto[j]
                        s.pop(a)
                        s.pop(b-1)
                        break
                    else:
                        texto.append(s[i])
        return "".join(s)
s = Solution()
s.reverseParentheses("(u(love)i)")