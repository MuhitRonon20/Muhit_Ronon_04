from typing import List


class Solution:

    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        parent = list(range(n))

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

            if root_u == root_v:
                return False

            parent[root_u] = root_v

        return True