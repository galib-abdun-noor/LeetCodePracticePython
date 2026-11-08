class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        dirs = [[1,0],[0,-1],[-1,0],[0,1]]
        row = len(grid)
        col = len(grid[0])
        edge = 0

        for i in range(row):
            for j in range(col):
                if grid[i][j] != 1:
                    continue

                for x,y in dirs:
                    ni, nj = i+x, j+y
                    if(ni>=0 and ni<row and nj>=0 and nj<col and grid[ni][nj] == 1):
                        continue
                    edge += 1

        return edge

if __name__ == "__main__":
    sol = Solution()
    grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
    print(sol.islandPerimeter(grid))
