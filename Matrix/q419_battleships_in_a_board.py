class Solution:
    def countBattleships(self, board: list[list[str]]) -> int:
        count = 0
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == ".":
                    continue
                if row>0 and board[row-1][col] == "X":
                    continue
                if col>0 and board[row][col-1] == "X":
                    continue
                count += 1

        return count

if __name__ == "__main__":
    sol = Solution()
    board = [["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]
    print(sol.countBattleships(board))