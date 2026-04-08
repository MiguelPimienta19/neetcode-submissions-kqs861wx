class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        ana = defaultdict(list)

        for s in strs:
            sorted_s = "".join(sorted(s))
            ana[sorted_s].append(s)
        
        return [list(num) for num in ana.values()]
