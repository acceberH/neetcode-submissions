class Solution:
    def partition(self, s: str) -> list[list[str]]:
        ans = []
        path = []
        
        def backtrack(start):
            if start == len(s):
                ans.append(path[:])
                return
            for end in range(start+1, len(s)+1):
                cut = s[start:end]
                if cut != cut[::-1]:
                    continue
                path.append(cut)
                backtrack(end)
                path.pop()
        backtrack(0)
        return ans
