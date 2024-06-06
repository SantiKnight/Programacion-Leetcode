class Solution:
    def addSpaces(self, s: str, spaces: list[int]) -> str:
        aux = []
        counter = 0
        tracker = 0
        while counter <= len(spaces):
            if counter == len(spaces):
                for item in s[tracker:]:
                    aux.append(item)
                break
            for item in s[tracker:spaces[counter]]:
                aux.append(item)
            tracker = spaces[counter]
            counter+=1
            aux.append(" ")
        
        frase = "".join(aux)
        return frase
s = Solution()
s.addSpaces("LeetcodeHelpsMeLearn",[8,13,15])