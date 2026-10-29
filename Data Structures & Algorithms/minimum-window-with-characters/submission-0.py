class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = defaultdict(int)
        cur_window = defaultdict(int)  # what we have rn

        right, left = 0, 0
        found = 0
        start = 0
        min_len = float("inf")

        for char in t:
            need[char] += 1

        total = len(need)

        while right < len(s):
            char = s[right]

            if char in need:
                cur_window[char] += 1

                if cur_window[char] == need[char]:
                    found += 1

            while found == total:

                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    start = left

                left_char = s[left]

                if left_char in need:
                    cur_window[left_char] -= 1

                    if cur_window[left_char] < need[left_char]:
                        found -= 1
                left += 1

            right += 1

        if min_len == float("inf"):
            return ""

        return s[start:start + min_len]