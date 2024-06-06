# Given a string array words, return an array of all characters that 
# show up in all strings within the words (including duplicates). You may return the answer in any order.

class Solution:
    def commonChars(self, words: list[str]) -> list[str]:
        result = []
        for letter in words[0]:
            for word in words:
                word = list(word)
                for item in result:
                    try:
                        word.remove(item)
                    except:
                        print("La letra no esta")
                if letter in word:
                    boolean = True
                else:
                    boolean = False
                if boolean == False:
                    break
            if boolean:
                result.append(letter)
s = Solution()
s.commonChars(["cool","lock","cook"])