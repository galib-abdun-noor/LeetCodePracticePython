from collections import deque
from uuid import MAX


class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        row = len(grid)
        col =  len(grid[0])
        dirs = [[1,0],[-1,0],[0,-1],[0,1]]
        maxArea = 0
        area = 0

        for i in range(row):
            for j in range(col):
                if grid[i][j] != 1:
                    continue

                grid[i][j] = 0
                queue = deque([(i,j)])
                area = 1

                while queue:
                    curri, currj = queue.popleft()
                    for x,y in dirs:
                        nexti, nextj = curri + x, currj + y
                        if(nexti >= 0 and nexti < len(grid) and nextj >= 0 and nextj < len(grid[0]) and grid[nexti][nextj] == 1):
                            grid[nexti][nextj] = 0
                            queue.append([nexti,nextj])
                            area += 1
                            maxArea = max(maxArea,area)

        return max(maxArea,area)

if __name__ == "__main__":
    sol = Solution()
    grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
    gridd = [[1]]
    print(sol.maxAreaOfIsland(grid))