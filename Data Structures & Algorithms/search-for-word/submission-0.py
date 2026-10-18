from typing import List


class Solution:

    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])

        def dfs(r: int, c: int, idx: int) -> bool:
            if idx == len(word):
                return True
            if (
                r < 0
                or r >= ROWS
                or c < 0
                or c >= COLS
                or board[r][c] != word[idx]
            ):
                return False

            temp = board[r][c]
            board[r][c] = "#"  

            found = (
                dfs(r + 1, c, idx + 1)
                or dfs(r - 1, c, idx + 1)
                or dfs(r, c + 1, idx + 1)
                or dfs(r, c - 1, idx + 1)
            )

            board[r][c] = temp  
            return found

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True

        return False