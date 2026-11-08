from collections import deque
from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        city = len(isConnected)
        visited = [False] * city
        provinces = 0

        for i in range(city):
            if visited[i]:
                continue
            provinces += 1
            queue = deque([i])

            while queue:
                current = queue.popleft()
                for n in range(city):
                    if isConnected[current][n] == 1 and not visited[n]:
                        queue.append(n)
                        visited[n] = True

        return provinces

if __name__ == "__main__":
    sol = Solution()
    isConnected = [[1,0,0],[0,1,0],[0,0,1]]
    isConnectedd = [[1,1,1],[1,1,1],[1,1,1]]
    print(sol.findCircleNum(isConnectedd))

