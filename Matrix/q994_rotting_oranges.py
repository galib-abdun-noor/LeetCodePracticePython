from collections import deque


class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        dirs = [[-1,0],[1,0],[0,-1],[0,1]]
        maxTime = 0
        fresh = 0
        queue = deque()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append([i,j,0])
                if grid[i][j] == 1:
                    fresh += 1

        while queue:
            curi, curj, time = queue.popleft()

            for x,y in dirs:
                nexti, nextj = curi + x, curj + y
                if nexti >= 0 and nexti < len(grid) and nextj >= 0 and nextj < len(grid[0]) and grid[nexti][nextj] == 1:
                    grid[nexti][nextj] = 2
                    fresh -= 1
                    queue.append([nexti,nextj,time + 1])
                    maxTime = max(maxTime,time+1)
        return maxTime if fresh == 0 else -1

if __name__ == "__main__":
    sol = Solution()
    grid = [[2,1,1],[1,1,0],[0,1,1]]
    print(sol.orangesRotting(grid))



