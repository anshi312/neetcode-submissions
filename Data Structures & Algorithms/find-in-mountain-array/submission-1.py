# mountainArr = [2,4,5,2,1], target = 2
# mountainArr = [2,4,5,6,3,2,1,0]  target = 3

class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        left = 0
        right = mountainArr.length() - 1

        while left < right:
            mid = (left + right) // 2
            mid_value = mountainArr.get(mid)
            next_value = mountainArr.get(mid + 1)

            if mid_value < next_value:
                left = mid + 1
            else:
                right = mid

        peak = left

        left = 0
        right = peak

        while left <= right:
            mid = (left + right) // 2
            mid_value = mountainArr.get(mid)
            if mid_value == target:
                return mid
            elif mid_value < target:
                left = mid + 1
            else:
                right = mid - 1

        left = peak
        right = mountainArr.length() - 1
        while left <= right:
            mid = (left + right) // 2
            mid_value = mountainArr.get(mid)
            if mid_value == target:
                return mid
            elif mid_value > target:
                left = mid + 1
            else:
                right = mid - 1
        
        return -1