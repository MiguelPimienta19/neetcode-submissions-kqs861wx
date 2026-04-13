class TimeMap:

    def __init__(self):
        self.keyStore = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.keyStore[key].append([value, timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        for val, ts in self.keyStore[key]:
            if ts <= timestamp:
                res = val
            # else:
            #     break
        return res



# class TimeMap:
#     def __init__(self):
#         self.keyStore = defaultdict(list)

#     def set(self, key: str, value: str, timestamp: int) -> None:
#         self.keyStore[key].append([value, timestamp])

#     def get(self, key: str, timestamp: int) -> str:
#         res, values = "", self.keyStore[key] #or if we use don't use defaultdict
#                         self.keyStore.get(key, [])
#         l, r = 0, len(values) - 1
#         while l <= r:
#             m = (l + r) // 2
#             if values[m][1] <= timestamp:
#                 res = values[m][0] #makes it the string
#                 l = m + 1
#             else:
#                 r = m - 1
#         return res