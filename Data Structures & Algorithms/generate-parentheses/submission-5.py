class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        path = []
        ans = []
        def dfs(openP, closeP):
            if len(path) == 2*n:
                ans.append("".join(path))
                return
            if openP < n:
                path.append("(")
                dfs(openP+1, closeP)
                path.pop()
            if closeP < openP:
                path.append(")")
                dfs(openP, closeP+1)
                path.pop()
        dfs(0,0)
        return ans