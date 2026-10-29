class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        right = 0 
        left = 0
        char = set()
        ans = 0
        while right < len(s):
            while s[right] in char:
                char.remove(s[left])
                left += 1
            char.add(s[right])
            ans = max(ans, right - left + 1)
            right += 1
        return ans




