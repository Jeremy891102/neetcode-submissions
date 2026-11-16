class Solution:
    def isPalindrome(self, s: str) -> bool:
        alpha = ''.join(c for c in s if c.isalnum())
        alpha = alpha.lower()
        alpha_reverse = alpha[::-1]
        return alpha == alpha_reverse