class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #---------minheap--------------------------------#

        # count = Counter(nums)

        # heap = []

        # for num, freq in count.items():
        #     heapq.heappush(heap, (freq, num))

        #     if len(heap) > k:
        #         heapq.heappop(heap)

        #     return [num for freq, num in heap]

        #---------freq count hashmap + sort -------------#

        count = {}
        for num in nums:
            count[num] = 1 + count.get(num,0)

        arr=[]
        for num, cnt in count.items():
            arr.append([cnt, num])
        arr.sort()

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res
        