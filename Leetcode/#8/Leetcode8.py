class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        valid = True
        p1 = []
        p2 = []
        p3 = []
        p4 = []
        p5 = []
        p6 = []
        p7 = []
        p8 = []
        p9 = []
        ps = [p1, p2, p3, p4, p5, p6, p7, p8, p9]

        for i in board:
            for k in range(0,10):
                if i.count(str(k))>1:
                    print(i)
                    return False
            counter = -1
            for j in i:
                counter += 1
                try:
                    j = int(j)
                except:
                    pass
                if ps[counter].__contains__(j) and j != '.':
                    return False
                else:
                    ps[counter].append(j)
        
        #HASTA ACA ESTA BIEN
        l1 = []
        l2 = []
        l3 = []
        for i in range(0,3):
            for j in range(0,3):
                if l1.__contains__(board[i][j]) and board[i][j] != ".":
                    return False
                else:
                    l1.append(board[i][j])
            for j in range(3,6):
                print(i, j)
                print(board[i][j])
                if l2.__contains__(board[i][j]) and board[i][j] != ".":
                    return False
                else:
                    l2.append(board[i][j])
            for j in range(6,9):
                if l3.__contains__(board[i][j]) and board[i][j] != ".":
                    return False
                else:
                    l3.append(board[i][j])
        
        l1 = []
        l2 = []
        l3 = []
        for i in range(3,6):
            for j in range(0,3):
                if l1.__contains__(board[i][j]) and board[i][j] != ".":
                    return False
                else:
                    l1.append(board[i][j])
            for j in range(3,6):
                if l2.__contains__(board[i][j]) and board[i][j] != ".":
                    return False
                else:
                    l2.append(board[i][j])
            for j in range(6,9):
                if l3.__contains__(board[i][j]) and board[i][j] != ".":
                    return False
                else:
                    l3.append(board[i][j])
        l1 = []
        l2 = []
        l3 = []
        for i in range(6,9):
            for j in range(0,3):
                if l1.__contains__(board[i][j]) and board[i][j] != ".":
                    return False
                else:
                    l1.append(board[i][j])
            for j in range(3,6):
                if l2.__contains__(board[i][j]) and board[i][j] != ".":
                    return False
                else:
                    l2.append(board[i][j])
            for j in range(6,9):
                if l3.__contains__(board[i][j]) and board[i][j] != ".":
                    return False
                else:
                    l3.append(board[i][j])
            
        return valid
s = Solution()
s.isValidSudoku([[".",".",".",".","5",".",".","1","."],[".","4",".","3",".",".",".",".","."],[".",".",".",".",".","3",".",".","1"],["8",".",".",".",".",".",".","2","."],[".",".","2",".","7",".",".",".","."],[".","1","5",".",".",".",".",".","."],[".",".",".",".",".","2",".",".","."],[".","2",".","9",".",".",".",".","."],[".",".","4",".",".",".",".",".","."]])