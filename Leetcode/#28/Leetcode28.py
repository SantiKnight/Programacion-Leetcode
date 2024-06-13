class Solution:
    def minMovesToSeat(self, seats: list[int], students: list[int]) -> int:
        seats.sort()
        students.sort()
        return sum(abs(students[i]-seats[i])for i in range(len(students)))
s = Solution()
s.minMovesToSeat([12,14,19,19,12],[19,2,17,20,7])