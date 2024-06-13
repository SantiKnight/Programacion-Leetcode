class Solution:
    def minMovesToSeat(self, seats: list[int], students: list[int]) -> int:
        total = 0
        seats = sorted(seats)
        students = sorted(students)
        for student in students:
            dif = abs(student-seats[0])
            seats.pop(0)
            total += dif
        return total
s = Solution()
s.minMovesToSeat([12,14,19,19,12],[19,2,17,20,7])