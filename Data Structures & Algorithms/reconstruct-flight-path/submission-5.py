class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for source, dest in tickets:
            graph[source].append(dest)

        for source in graph:
            graph[source].sort(reverse=True)

        result = []
        def dfs(source):
            while graph[source]:
                next_dest = graph[source].pop()
                dfs(next_dest)
            result.append(source)

        dfs("JFK")
        result.reverse()
        return result