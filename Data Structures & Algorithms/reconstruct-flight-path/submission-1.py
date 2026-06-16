class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for source, dest in tickets:
            graph[source].append(dest)

        for source in graph:
            graph[source].sort(reverse = True)

        result = []

        def dfs(airport):
            while graph[airport]:
                next_airport = graph[airport].pop()
                dfs(next_airport)
            result.append(airport)

        dfs("JFK")
        return result[::-1]           