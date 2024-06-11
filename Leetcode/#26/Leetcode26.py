class Solution:
    def relativeSortArray(self, arr1: list[int], arr2: list[int]) -> list[int]:
        aux = []
        for element in arr2:
            cant = arr1.count(element)
            aux.extend([element] * cant)
            while element in arr1:
                arr1.remove(element)
        aux.extend(sorted(arr1))
        return aux
            
s = Solution()
s.relativeSortArray([2,3,1,3,2,4,6,7,9,2,19],[2,1,4,3,9,6])