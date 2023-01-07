
from collections import defaultdict, deque
class Solution:
    def solve(self, edges):
        graph = defaultdict(list)
        weights = {}
        max_weight = 0
        N = 0
        for u, v, w in edges:
            graph[u].append(v)
            graph[v].append(u)
            weights[u, v] = w
            weights[v, u] = w
            N = max(N, u + 1, v + 1)
            max_weight = max(max_weight, w)
        def bfs(root, weight_cap):
            target = N - 1
            Q = deque([(root, 0, 0)])
            visited = [False] * N
            visited[0] = True
            while Q:
                v, d, current_weight = Q.pop()
                if v == N - 1:
                    return d, current_weight
                for w in graph[v]:
                    if visited[w]:
                        continue
                    new_weight = weights[v, w]
                    if new_weight <= weight_cap:
                        visited[w] = True
                        Q.appendleft((w, d + 1, max(current_weight, new_weight)))
            return -1, -1
        result = float("inf")
        while max_weight >= 0:
            d, weight = bfs(0, max_weight)
            if d >= 0:
                result = min(result, d * weight)
                max_weight = weight - 1
            else:
                break
        return result if result < float("inf") else -1

ob = Solution()
graph = [
    [0, 1, 1],
    [1, 2, 1],
    [2, 3, 1],
    [3, 4, 1]
]

value = (ob.solve(graph))

if value == len(graph):
    print("Possible")
else:
    print("Impossible")
