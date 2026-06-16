class TrieNode:
    def __init__(self):
        self.children = {}
        self.wordend = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()

        for word in words:
            curr = root
            for ch in word:
                if ch not in curr.children:
                    curr.children[ch] = TrieNode()
                curr = curr.children[ch]
            curr.wordend = word

        rows = len(board)
        cols = len(board[0])

        result = []

        def dfs(r, c, node):
            ch = board[r][c]
            if ch not in node.children: return

            nxt = node.children[ch]

            if nxt.wordend:
                result.append(nxt.wordend)
                nxt.wordend = None

            board[r][c] = '#'

            for dr, dc in [(1,0),(0,1),(-1,0),(0,-1)]:
                nr = r + dr
                nc = c + dc

                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != '#':
                    dfs(nr, nc, nxt)

            board[r][c] = ch

            if not nxt.children and nxt.wordend is True:
                del node.children[ch]

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root)

        return result