class Solution(object):
    def containe_path(self, board, word, i, j, position, visited):
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[i]) or (i, j) in visited or board[i][j] != word[position]:
            return False
        if position == len(word) - 1:
            return True
        visited.add((i, j))
        res = (
            self.containe_path(board, word, i, j + 1, position + 1, visited) or
            self.containe_path(board, word, i, j - 1, position + 1, visited) or
            self.containe_path(board, word, i + 1, j, position + 1, visited) or
            self.containe_path(board, word, i - 1, j, position + 1, visited)
        )
        visited.remove((i, j))
        return res

    def exist(self, board, word):
        for i in word:
            found = False
            for j in board:
                if i in j:
                    found = True
                    break
            if not found:
                return False
        visited = set()
        for i in range(len(board)):
            for j in range(len(board[i])):
                if self.containe_path(board, word, i, j, 0, visited):
                    return True

        return False