from bisect import bisect_right
class TimeMap:

    def __init__(self):
        self.data = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.data:
            self.data[key] = []
        self.data[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.data:
            return ""
        
        entries = self.data[key]
        
        # Binary search to find the insertion point
        low, high = 0, len(entries) - 1
        while low <= high:
            mid = (low + high) // 2
            if entries[mid][0] == timestamp:
                return entries[mid][1]
            elif entries[mid][0] < timestamp:
                low = mid + 1
            else:
                high = mid - 1

        # If not found, return the value associated with the largest timestamp_prev
        return "" if high < 0 else entries[high][1]
# T.C: def set takes O(1) appending to list; def get performs bisect_right, takes O(logn) time; O(n) for creating timestamps list
# S.C: O(n) , no.of time stamped entries across all the keys


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)