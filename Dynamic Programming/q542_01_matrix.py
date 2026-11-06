from collections import deque
from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        queue = deque()
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                if mat[row][col] == 0:
                    queue.append([row,col,0])
                else:
                    mat[row][col] = float("inf")

        dirs = [[0,-1],[0,1],[1,0],[-1,0]]

        while queue:
            currX, currY, dist = queue.popleft()
            for x,y in dirs:
                nextX, nextY, nextVal = currX + x, currY + y, dist + 1
                if nextX < 0 or nextX >= len(mat) or nextY < 0 or nextY >= len(mat[0]):
                    continue
                if mat[nextX][nextY] == float("inf"):
                    mat[nextX][nextY] = nextVal
                    queue.append([nextX,nextY,nextVal])

        return mat

if __name__ == "__main__":
    sol = Solution()
    mat = [[0,0,0],[0,1,0],[1,1,1]]
    matt = [[0,0,0],[0,1,0],[0,0,0]]

    print(sol.updateMatrix(matt))

