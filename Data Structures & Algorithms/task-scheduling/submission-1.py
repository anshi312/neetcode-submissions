# A A A A --> A___A___A___A
# most_freq = 4
# gaps_req = 3 --> max_freq - 1
# each gap must be size n --> A + n gaps --> n + 1 size

# thus, total size:
# add final task: (max_frea - 1) * (n + 1) + max_count


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0:
            return len(tasks)

        freq_map = defaultdict(int)
        for task in tasks:
            freq_map[task] += 1
        
        max_freq = max(freq_map.values())

        max_count = 0
        for value in freq_map.values():
            if value == max_freq:
                max_count += 1

        size = (max_freq - 1) * (n + 1) + max_count

        return max(size, len(tasks))
