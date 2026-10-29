class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        right = 0
        left = 0
        ans = 0
        count = {}
        

        while right < len(s):
            if s[right] not in count:

                count[s[right]] = 1
            else:
                
                count[s[right]] += 1

            while (right - left + 1) - max(count.values()) > k:
                count[s[left]] -= 1
                left += 1

            ans = max(ans, right - left + 1)
            right += 1
            

        return ans
