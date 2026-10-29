class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count_s1 = {}
        window = {}
        left = 0

        for char in s1:
            if char not in count_s1:
                count_s1[char] = 1
            else:
                count_s1[char] += 1

        for right in range(len(s2)):

            if s2[right] not in window:
                window[s2[right]] = 1
            else:
                window[s2[right]] += 1

            if right - left + 1 > len(s1):
                window[s2[left]] -= 1

                if window[s2[left]] == 0:
                    del window[s2[left]]

                left += 1

            if right - left + 1 == len(s1):
                if window == count_s1:
                    return True

        return False