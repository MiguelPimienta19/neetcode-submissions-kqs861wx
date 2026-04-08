# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        #since this is binary tree traversae im gonna do bfs it 
        # it literally what this is asking me to do
        res = [] 
        q = deque()
        q.append(root)

        while q:
            length = len(q)
            level = [] #what we are appending
            for i in range(length):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level: #because we will get an empty list once finished
                res.append(level)

        return res
        
        