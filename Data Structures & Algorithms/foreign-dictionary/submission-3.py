class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph = defaultdict(set)
        indegree = {c : 0 for w in words for c in w}
        # indegree = {}
        # for w in words:
        #     for c in w:
        #         indegree[c] = 0

        for w1, w2 in zip(words, words[1:]):
            if len(w1) > len(w2) and w1.startswith(w2):
                return ""
            # checks abc, ab --> this is invalid
            

            for c1, c2 in zip(w1, w2):
                if c1 != c2:
                    if c2 not in graph[c1]:
                        graph[c1].add(c2)
                        indegree[c2] += 1
                    break
            
        queue = deque([c for c in indegree if indegree[c] == 0])
        order = []

        while queue:
            c = queue.popleft()
            order.append(c)

            for nbh in graph[c]:
                indegree[nbh] -= 1
                if indegree[nbh] == 0:
                    queue.append(nbh)

        if len(order) < len(indegree):
            return ""

        return "".join(order)