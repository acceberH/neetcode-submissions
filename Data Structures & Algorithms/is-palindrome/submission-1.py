class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = []

        for char in s:
            if char.isalnum():
                lower_char = char.lower()
                clean.append(lower_char)

        return clean == clean[::-1]