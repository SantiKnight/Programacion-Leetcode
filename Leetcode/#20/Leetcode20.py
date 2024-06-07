class Solution:
    def vowelStrings(self, words: list[str], left: int, right: int) -> int:
        contador = 0
        for word in words[left:right+1]:
            print(word)
            word = list(word)
            print(word[0], word[-1])
            if word[0] in ["a","e","i","o","u"] and word[-1] in ["a","e","i","o","u"]:
                contador +=1
        return contador