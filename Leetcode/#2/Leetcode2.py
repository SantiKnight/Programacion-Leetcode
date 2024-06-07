class Solution:
    def romanToInt(self, s: str) -> int:
        dicc = dict({'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000})
        suma = 0
        s = list(s)
        iterador = iter(s)
        siguiente = next(iterador)
        for item in s:
            try:
                siguiente = next(iterador)
            except Exception as exc:
                print(exc)
            if item in ['I', 'X', 'C']:
                if item == 'I' and siguiente in ['V', 'X']:
                    suma -= dicc[item]
                elif item == 'X' and siguiente in ['L', 'C']:
                    suma -= dicc[item]
                elif item == 'C' and siguiente in ['D', 'M']:
                    suma -= dicc[item]
                else:
                    suma += dicc[item]
            else:
                suma += dicc[item]
        print(suma)
        
s = Solution()
s.romanToInt('MCDXLIV')