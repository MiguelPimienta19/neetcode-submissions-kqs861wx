class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for i in nums:
            if i not in count:
                count[i] = 0
            count[i] += 1
        
        # Step 2: Create a singular list containing all (number, frequency) pairs
        freq_list = []  # Singular list
        for key, value in count.items():
            freq_list.append((key, value))  # Append each number with its frequency

        # Step 3: Sort the singular list based on the frequency
        for i in range(len(freq_list)):
            for j in range(i + 1, len(freq_list)):
                if freq_list[i][1] < freq_list[j][1]:  # Compare frequencies
                    # Swap to ensure higher frequency comes first
                    freq_list[i], freq_list[j] = freq_list[j], freq_list[i]

        # Step 4: Extract the top k numbers from the sorted list
        res = []
        for i in range(k):
            res.append(freq_list[i][0])  # Append the number, not the frequency

        return res