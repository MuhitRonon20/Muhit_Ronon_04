from collections import defaultdict


class Solution:

    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        res = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            # Use tuple of counts as dictionary key
            res[tuple(count)].append(s)

        return list(res.values())