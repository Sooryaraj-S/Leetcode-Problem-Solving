class Solution(object):
    #Generate the board
    def totalNQueens(self, n):
        self.n=n
        self.result=[]
        board=[["."for i in range(n)]for i in range (n)]
        self.solve_nqueens(board,0)
        return len(self.result) #return the length -> int

    #to check whether the position is safe
    def is_safe(self,board,row,col):
        for i in range(row):
            if board[i][col]=="q":
                return False
        i,j=row,col
        while i>=0 and j>=0:
            if board[i][j]=="q":
                return False
            i-=1
            j-=1
        i,j=row,col
        while i>=0 and j<self.n:
            if board[i][j]=="q":
                return False
            i-=1
            j+=1
        return True

       

    def solve_nqueens(self,board,row):
        if row==self.n:
            self.result.append(self.solution(board))
            return
        for col in range(self.n):
            if self.is_safe(board, row, col):
                board[row][col]="q"
                self.solve_nqueens(board,row+1)
                board[row][col]="."
    def solution(self,board):
        return [''.join(row) for row in board] #to convert the list elements into an single string  eg: ".Q.."
            
    











        