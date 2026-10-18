from typing import List


class TrieNode:

    def __init__(self):
        self.children = {}
        self.word = None


class Solution:

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            curr = root
            for char in word:
                if char not in curr.children:
                    curr.children[char] = TrieNode()
                curr = curr.children[char]
            curr.word = word

        ROWS, COLS = len(board), len(board[0])
        res = []

        def dfs(r: int, c: int, parent_node: TrieNode) -> None:
            char = board[r][c]
            curr_node = parent_node.children[char]

            if curr_node.word:
                res.append(curr_node.word)
                curr_node.word = None

            board[r][c] = "#"

            for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                nr, nc = r + dr, c + dc
                if (
                    0 <= nr < ROWS
                    and 0 <= nc < COLS
                    and board[nr][nc] in curr_node.children
                ):
                    dfs(nr, nc, curr_node)

            board[r][c] = char

            if not curr_node.children:
                del parent_node.children[char]

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] in root.children:
                    dfs(r, c, root)

        return res