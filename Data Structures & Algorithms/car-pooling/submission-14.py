class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # points = []
        # for passengers, start, end in trips:
        #     points.append([start, passengers])
        #     points.append([end, -passengers])

        # points.sort()
        # curPass = 0
        # for point, passengers in points:
        #     curPass += passengers
        #     if curPass > capacity:
        #         return False

        # return True

        trips.sort(key=lambda t: t[1])

        heap = []
        curr_pass = 0

        for num_pass, start, end in trips:
            while heap and heap[0][0] <= start:
                h_end, h_num = heapq.heappop(heap)
                curr_pass -= h_num

            curr_pass += num_pass
            
            if curr_pass > capacity:
                return False

            heapq.heappush(heap, (end, num_pass))
        
        return True