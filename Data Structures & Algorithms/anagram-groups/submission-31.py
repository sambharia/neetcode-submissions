class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        new_hashmap = {}
        for str in strs:
            no_duplicate = tuple(sorted(str)) # i
            if no_duplicate not in new_hashmap.keys():
                new_hashmap[no_duplicate] = [str]
            else:
                new_hashmap[no_duplicate].append(str) 

        return list(new_hashmap.values())



