class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        new_hashmap = defaultdict(list)

        for s in strs:
            count = [0] * 26

            for character in s:
                count[ord(character) - ord('a')] += 1
            new_hashmap[tuple(count)].append(s)
        return list(new_hashmap.values())
    