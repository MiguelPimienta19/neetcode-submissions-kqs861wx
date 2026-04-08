class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash = defaultdict(list) #just creates a hash map with empty list orginally

        for word in strs:
            count = [0] * 26 #for the 26 letters in alph

            for letter in word:
                count[ord(letter) - ord("a")] += 1

            hash[tuple(count)].append(word)

        return hash.values()

