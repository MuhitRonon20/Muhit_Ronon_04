from typing import List


class Solution:

    def canFinish(
        self, numCourses: int, prerequisites: List[List[int]]
    ) -> bool:
        indegree = [0] * numCourses
        adj = [[] for _ in range(numCourses)]

        for dest, src in prerequisites:
            indegree[dest] += 1
            adj[src].append(dest)

        q = [i for i in range(numCourses) if indegree[i] == 0]
        head = 0

        while head < len(q):
            curr = q[head]
            head += 1

            for neighbor in adj[curr]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)

        return head == numCourses