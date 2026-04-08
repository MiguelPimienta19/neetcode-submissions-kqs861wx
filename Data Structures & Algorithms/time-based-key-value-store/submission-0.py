class TimeMap:

    def __init__(self):
        self.stamps = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        #should be O(1) its a hashmap.
        if key not in self.stamps:
            self.stamps[key] = []
        self.stamps[key].append([value,timestamp])

    def get(self, key: str, timestamp: int) -> str:
        # should be O(logn) binary search.
        res = ""#found no value
        values = self.stamps.get(key, []) #use get because dict function. grabs the values and if not just reutrns empty list
        print(values)
        
        
        l, r = 0, len(values) -1

        while l <= r:
            m = (l + r) // 2
            if timestamp >= values[m][1]: #at m postion checks the timestamp.
                res = values[m][0] #at the m postion set res to [value, timestamp] value!!
                l = m + 1
            else:
                r = m - 1
        return res