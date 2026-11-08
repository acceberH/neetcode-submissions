class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        path, ans = [], []

        def dfs(left, right):
            if right == n:
                ans.append("".join(path))
                return
            if left < n:
                path.append("(")
                dfs(left+1, right)
                path.pop()
            if right < left:
                path.append(")")
                dfs(left, right+1)
                path.pop()
        dfs(0,0)
        return ans

