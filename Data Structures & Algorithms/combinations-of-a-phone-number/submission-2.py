class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {"2": "abc", 
        "3": "def", 
        "4": "ghi", 
        "5": "jkl", 
        "6": "mno", 
        "7": "pqrs", 
        "8": "tuv", 
        "9": "wxyz"}
        if not digits:
            return []
        path, ans = [], []
        def dfs(i):
            if i == len(digits):
                ans.append("".join(path))#[dg dh di eg]
                return
            for char in mapping[digits[i]]:
                path.append(char)#[e g ]
                dfs(i+1)
                path.pop()
        dfs(0)
        return ans
        #time complexity: O(n*4^n) space complexity: O(n*4^n)
            
