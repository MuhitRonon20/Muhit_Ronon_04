from typing import List


class Solution:

    def foreignDictionary(self, words: List[str]) -> str:
        present = [False] * 26
        for word in words:
            for ch in word:
                present[ord(ch) - 97] = True

        unique_count = sum(present)

        adj = [[] for _ in range(26)]
        indegree = [0] * 26
        has_edge = [[False] * 26 for _ in range(26)]

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            min_len = min(len(w1), len(w2))

            if len(w1) > len(w2) and w1[:min_len] == w2:
                return ""

            for j in range(min_len):
                if w1[j] != w2[j]:
                    u = ord(w1[j]) - 97
                    v = ord(w2[j]) - 97
                    if not has_edge[u][v]:
                        has_edge[u][v] = True
                        adj[u].append(v)
                        indegree[v] += 1
                    break

        q = [i for i in range(26) if present[i] and indegree[i] == 0]
        head = 0
        res = []

        while head < len(q):
            u = q[head]
            head += 1
            res.append(chr(u + 97))
            for v in adj[u]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    q.append(v)

        return "".join(res) if len(res) == unique_count else ""