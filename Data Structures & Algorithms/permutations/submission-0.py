class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        path = [] #num = [3, 5]
        ans = []
        visited = [False] * len(nums)
        def dfs(i):
            if len(path) == len(nums):
                ans.append(path[:])
                return
            for j in range(len(nums)):
                if visited[j]:
                    continue
                visited[j] = True
                path.append(nums[j])
                dfs(i+1)
                path.pop()
                visited[j] = False
        dfs(0)
        return ans
 # O(n!*n) 
                
            