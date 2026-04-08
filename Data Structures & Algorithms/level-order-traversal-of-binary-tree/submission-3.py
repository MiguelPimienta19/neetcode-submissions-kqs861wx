# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        q = deque([root])
        res = []

        while q:
            level = [] #make new list every level
            #not sure what would go here but for now lets just loop
            for i in range(len(q)):
                node = q.popleft() #we pop our left

                if node: #make sure its not null
                    level.append(node.val) #append the value to our level then add to our bfs
                    q.append(node.left)
                    q.append(node.right)
            if level: #edge case. where we reach a null leaf.
                res.append(level)
            
        return res
            



