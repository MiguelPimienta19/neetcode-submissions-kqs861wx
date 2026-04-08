class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {}

        def dfs(i, j):
            # if we've exhausted word1, we must insert the rest of word2
            if i == len(word1):
                return len(word2) - j
            # if we've exhausted word2, we must delete the rest of word1
            if j == len(word2):
                return len(word1) - i

            # Check memo
            if (i, j) in memo:
                return memo[(i, j)]

            if word1[i] == word2[j]:
                memo[(i, j)] = dfs(i + 1, j + 1)
            else:
                # Delete word1[i] → move i forward, j stays the same
                delete_cost  = dfs(i + 1, j)
                # Insert word2[j] into word1 → move j forward, i stays the same
                insert_cost  = dfs(i, j + 1)
                # Replace word1[i] with word2[j] → move both forward
                replace_cost = dfs(i + 1, j + 1)
                # Pick the cheapest operation and add 1 for the cost of doing it
                memo[(i, j)] = 1 + min(delete_cost, insert_cost, replace_cost)
            return memo[(i, j)]

        return dfs(0, 0)

