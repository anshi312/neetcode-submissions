# 5555
# deadends = 0120   1111    2020    3333

# 4444
# 4443 4445 4434 4454 4344 4544 3444 5444

# check if digit + 1 and digit - 1 is in position of digit in deadends

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:

        dead_set = set()
        for i in range(len(deadends)):
            dead_set.add(deadends[i])

        if "0000" in dead_set:
            return -1
        
        if target == "0000":
            return 0

        visited_set = set()
        visited_set.add("0000")

        queue = deque()
        queue.append(("0000", 0))
        
        while queue:
            state, steps = queue.popleft()

            if state == target:
                return steps

            for i in range(4):
                digit = int(state[i])

                up_digit = (digit + 1) % 10
                down_digit = (digit - 1 + 10) % 10

                new_state_up = state[ : i] + str(up_digit) + state[i + 1 : ]
                new_state_down = state[ : i] + str(down_digit) + state[ i + 1 : ]

                for nbh in [new_state_up, new_state_down]:
                    if nbh not in visited_set and nbh not in dead_set:
                        visited_set.add(nbh)
                        queue.append((nbh, steps + 1))

        return -1