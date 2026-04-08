# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        #we are going to use dfs. ohh between 3 and 8 return 5

        #given second picuture 


        def dfs(node, p, q):
            if not node or not p or not q:
                return None

            if node.val > p.val and q.val < node.val:
                return dfs(node.left,p,q)
            
            elif node.val < q.val and p.val > node.val:
                return dfs(node.right,p,q)

            else:
                return node
        
        return dfs(root, p, q)
            

