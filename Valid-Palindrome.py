class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        clipped_string = \\
        for ch in s:
            if ch.isalnum():
                clipped_string += ch
        return clipped_string == clipped_string[::-1]