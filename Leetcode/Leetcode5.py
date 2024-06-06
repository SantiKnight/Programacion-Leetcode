class Solution:
    def maxScoreWords(self, words: list[str], letters: list[str], score: list[int]) -> int:
        abc = {'a': None, 'b': None, 'c': None, 'd': None, 'e': None, 'f': None, 'g': None, 'h': None, 'i': None, 'j': None, 'k': None, 'l': None, 'm': None, 'n': None, 'o': None, 'p':None , 'q':None , 'r': None, 's': None, 't': None, 'u': None, 'v': None, 'w': None, 'x': None, 'y': None, 'z': None}
        abc2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        index = 0
        totalValue = 0
        flag = True
        lettersAux = letters
        for l in abc2:
            abc[l] = score[index]
            index += 1
        #HASTA ACA ESTA BIEN
        letters_count: list[int] = [0 for _ in range(26)]
        for letter in letters:
            ind: int = ord(letter) - 97
            letters_count[ind] += 1
        print(letters_count)
        
        words_scores: dict[str, int] = {}
        for word in words:
            s = 0
            for char in word:
                ind = ord(char) - 97
                s += score[ind]
            words_scores[word] = s
            
        print(words_scores)
        
        lAux = lettersAux
        for word in words:
            flag = True
            lettersAux = lAux
            wordValue = 0 
            for letra in word:
                if flag == False:
                    flag = True
                    break
                for j in range(len(lAux)):
                    if letra in lAux:
                        if letra == lAux[j]:
                            wordValue += abc[letra]
                            lAux.pop(j)
                            break
                    else:
                        wordValue = 0
                        flag = False
                        lAux = lettersAux
                        break
                    
                    #la concha de tu madre
                    
            print(word, wordValue)
            totalValue += wordValue
            print(totalValue)
s = Solution()
s.maxScoreWords(["dog","cat","dad","good"],["a","a","c","d","d","d","g","o","o"],[1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0])