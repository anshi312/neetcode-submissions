class Solution:

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def canShip(cap):
            days_used = 1
            current_load = 0

            for weight in weights:
                if current_load + weight > cap:
                    days_used += 1
                    current_load = 0
                current_load += weight

            return days_used <= days

        left = max(weights)
        right = sum(weights)

        while left < right:
            mid = (left + right) // 2
            
            if canShip(mid):
                right = mid
            else:
                left = mid + 1

        return left