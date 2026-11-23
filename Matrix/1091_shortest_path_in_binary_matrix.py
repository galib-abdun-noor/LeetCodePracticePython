from collections import deque


class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        n = len(grid)

        if(grid[0][0] != 0  or grid[n-1][n-1] != 0):
            return -1

        direc = [
            (-1, -1),(-1, 0),(-1, 1),
            (0, -1),        (0, 1),
            (1, -1), (1, 0), (1, 1)
        ]

        queue = deque([(0, 0, 1)])
        grid[0][0] = 1

        while queue:
            r, c, length = queue.popleft()

            if r == n-1 and c == n-1:
                return length

            for i,j in direc:
                nr, nc = r+i, c+j
                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0:
                    queue.append((nr, nc, length + 1))
                    grid[nr][nc] = 1

        return -1

if __name__ == "__main__":
    sol = Solution()
    grid = [[0,0,0],[1,1,0],[1,1,0]]
    grid1 = [[0,0,0,0,1],[1,0,0,0,0],[0,1,0,1,0],[0,0,0,1,1],[0,0,0,1,0]]

    print(sol.shortestPathBinaryMatrix(grid1))

