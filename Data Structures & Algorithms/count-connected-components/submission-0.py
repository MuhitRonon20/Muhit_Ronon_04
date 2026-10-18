from typing import List


class Solution:

    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = list(range(n))
        rank = [1] * n
        components = n

        def find(i: int) -> int:
            root = i
            while root != parent[root]:
                root = parent[root]
            curr = i
            while curr != root:
                nxt = parent[curr]
                parent[curr] = root
                curr = nxt
            return root

        for u, v in edges:
            root_u = find(u)
            root_v = find(v)

            if root_u != root_v:
                if rank[root_u] < rank[root_v]:
                    parent[root_u] = root_v
                elif rank[root_u] > rank[root_v]:
                    parent[root_v] = root_u
                else:
                    parent[root_v] = root_u
                    rank[root_u] += 1
                components -= 1

        return components