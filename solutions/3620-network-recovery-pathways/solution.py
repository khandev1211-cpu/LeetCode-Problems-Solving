from typing import List
from collections import deque

class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        n = len(online)

        adj_all = [[] for _ in range(n)]
        indeg = [0] * n
        for u, v, c in edges:
            adj_all[u].append((v, c))
            indeg[v] += 1

        # topological order (graph is guaranteed a DAG)
        topo = []
        dq = deque([i for i in range(n) if indeg[i] == 0])
        indeg_copy = indeg[:]
        while dq:
            u = dq.popleft()
            topo.append(u)
            for v, c in adj_all[u]:
                indeg_copy[v] -= 1
                if indeg_copy[v] == 0:
                    dq.append(v)

        if not edges:
            return -1

        costs_sorted = sorted(set(c for _, _, c in edges))
        INF = float('inf')

        def feasible(threshold: int) -> bool:
            dist = [INF] * n
            dist[0] = 0
            for u in topo:
                if dist[u] == INF:
                    continue
                if u != 0 and u != n - 1 and not online[u]:
                    continue
                du = dist[u]
                for v, c in adj_all[u]:
                    if c >= threshold:
                        nd = du + c
                        if nd < dist[v]:
                            dist[v] = nd
            return dist[n - 1] <= k

        lo, hi = 0, len(costs_sorted) - 1
        ans = -1
        while lo <= hi:
            mid = (lo + hi) // 2
            if feasible(costs_sorted[mid]):
                ans = costs_sorted[mid]
                lo = mid + 1
            else:
                hi = mid - 1
        return ans