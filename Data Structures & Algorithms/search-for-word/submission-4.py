class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        def dfs(r, c, i):
            if i == len(word):
                return True
            if r<0 or r>=m or c<0 or c>=n:
                return False
            if board[r][c] != word[i]:
                return False
            
            original = board[r][c]
            board[r][c] = "/"
            find = (dfs(r+1, c, i+1) or dfs(r-1, c, i+1) or dfs(r, c+1, i+1) or dfs(r, c-1, i+1))
            board[r][c] = original
            return find
        for r in range(m):
            for c in range(n):
                if dfs(r, c, 0):
                    return True
        return False