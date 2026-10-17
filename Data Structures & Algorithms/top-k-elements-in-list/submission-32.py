class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1

        reverse_dict = {}
        for key, value in counts.items():
            if value not in reverse_dict:
                reverse_dict[value] = []
            reverse_dict[value].append(key)

        reverse_counts = sorted(reverse_dict)

        final_list = []

        for count in range(len(reverse_counts)):
            frequency = reverse_counts[-(count + 1)]
            for num in reverse_dict[frequency]:
                final_list.append(num)
                if len(final_list) == k:
                    return final_list