class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList: return 0

        wordList.append(beginWord)

        patterns = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[(i+1):]
                patterns[pattern].append(word)

        queue = deque()
        queue.append((beginWord, 1))
        visited = set()
        visited.add(beginWord)

        while queue:
            word, steps = queue.popleft()

            for i in range(len(word)):
                pattern = word[:i] + "*" + word[1+i:]

                for nbh in patterns[pattern]:
                    if nbh == endWord:
                        return steps + 1

                    if nbh not in visited:
                        visited.add(nbh)
                        queue.append((nbh, steps+1))

                patterns[pattern] = []

        return 0