from collections import deque
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        island = 0
        row = len(grid)
        col =  len(grid[0])
        dirs = [[1,0],[-1,0],[0,-1],[0,1]]

        for i in range(row):
            for j in range(col):
                if grid[i][j] != "1":
                    continue

                island += 1
                grid[i][j] = 0
                queue = deque([(i,j)])

                while queue:
                    curri, currj = queue.popleft()
                    for x,y in dirs:
                        nexti, nextj = curri + x, currj + y
                        if(nexti >= 0 and nexti < len(grid) and nextj >= 0 and nextj < len(grid[0]) and grid[nexti][nextj] == "1"):
                                grid[nexti][nextj] = 0
                                queue.append([nexti,nextj])

        return island


if __name__ == "__main__":
    sol = Solution()
    grid = [
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
    ]
    gridd = [["1","1","1"],["0","1","0"],["1","1","1"]]
    print(sol.numIslands(gridd))