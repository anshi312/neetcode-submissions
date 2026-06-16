class TimeMap:

    def __init__(self):
        self.key_store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.key_store:
            self.key_store[key] = []
        self.key_store[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.key_store:
            self.key_store[key] = []
        
        key_values = self.key_store[key]

        # key_values = [[1, val1], [2, val2]]

        left = 0
        right = len(key_values) - 1

        while left <= right:
            mid = (left + right) // 2
            if key_values[mid][0] <= timestamp:
                left = mid + 1
            else:
                right = mid - 1
        
        if right >= 0:
            result = key_values[right][1]
        else:
            result = ""
        return result

#---------- what if timestamps are not sorted------------#

'''
    def __init__(self):
        self.key_store = {}

    def set(self, key, value, timestamp):
        if key not in self.key_store:
            self.key_store[key] = []
        
        key_values = self.key_store[key]

        timestamps = [pair[0] for pair in key_values]

        index = bisect.bisect_left(timestamps, timestamp)

        key_values.insert(index, [timestamp, value])

    def get(self, key, timestamp):
        if key not in self.key_store:
            self.key_store[key] = []
        
        key_values = self.key_store[key]
        
'''