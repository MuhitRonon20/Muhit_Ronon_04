from collections import Counter


class Solution:

    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = Counter(nums)
        # Buckets where index represents frequency
        freq = [[] for _ in range(len(nums) + 1)]

        for num, cnt in count.items():
            freq[cnt].append(num)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
        return res