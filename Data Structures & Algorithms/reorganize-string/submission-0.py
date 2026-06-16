class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = Counter(s)

        max_freq = max(freq.values())
        if max_freq > (len(s) + 1) // 2:
            return ""

        heap = []        
        for char, count in freq.items():
            heapq.heappush(heap, (-count, char))

        result = []
        prev_count = 0
        prev_char = ""
        while heap:
            count, char = heapq.heappop(heap)
            result.append(char)

            if prev_count < 0:
                heapq.heappush(heap, (prev_count, prev_char))

            count += 1
            prev_count, prev_char = count, char

        return "".join(result)