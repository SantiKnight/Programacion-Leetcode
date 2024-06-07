class Solution:
    def replaceWords(self, dictionary: list[str], sentence: str) -> str:
        contador = 0
        lista = sentence.split()
        for word in lista:
            frase_minima = word
            minimo = 100
            for frase in dictionary:
                if word.startswith(frase):
                    if minimo > len(frase):
                        minimo = len(frase)
                        frase_minima = frase
            lista[contador] = frase_minima
            contador += 1
        result = " ".join(lista)
        return result
        
s = Solution()
s.replaceWords(["a","b","c"], "aadsfasf absbs bbab cadsfafs")