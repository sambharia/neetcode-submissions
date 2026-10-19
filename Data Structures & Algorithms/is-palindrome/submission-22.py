class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) -1
        newStr = ""
        for c in s:
            if c.isalnum():
                newStr += c.lower()
        return newStr == newStr[::-1]