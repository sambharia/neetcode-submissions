
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}

        for num in nums:
            counts[num] = counts.get(num, 0) + 1

        new_counts = sorted(counts.values(), reverse=True)

        final_list = []

        for new_count in range(k):
            for key, value in counts.items():
                if value == new_counts[new_count] and key not in final_list:
                    final_list.append(key)
                    break

        return final_list
