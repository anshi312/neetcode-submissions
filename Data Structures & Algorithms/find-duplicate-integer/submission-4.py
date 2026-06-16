class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast: break

        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow

# 1️⃣ First loop: detect a cycle
# 	•	Treat the array like a linked list: i → nums[i]
# 	•	slow moves 1 step, fast moves 2 steps
# 	•	When they meet → you’re inside the cycle (duplicate exists)

# 2️⃣ Second loop: find the cycle entry
# 	•	Reset a pointer (slow2) to start
# 	•	Move slow and slow2 one step at a time
# 	•	Where they meet = cycle entry

# 3️⃣ Return the meeting value
# 	•	That index/value is the duplicate