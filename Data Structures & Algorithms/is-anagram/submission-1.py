class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts = {}
        counts2 = {}
        for letter in s:
            counts[letter] = counts.get(letter, 0) + 1
        for letter in t:
            counts2[letter] = counts2.get(letter, 0) + 1

        if counts == counts2:
            return True

        return False