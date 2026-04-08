class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        good = set()

        for t in triplets:
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue #makes sure all three elements are less then the target so it can work
            #as in skip it.
            for i, v in enumerate(t):
                if v == target[i]:
                    good.add(i)
        return len(good) == 3
