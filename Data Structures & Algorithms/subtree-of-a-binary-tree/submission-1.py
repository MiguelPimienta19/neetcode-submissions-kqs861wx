# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        if not subRoot:
            return True #root tree has null. 
        if not root:
            return False #root needs to be there for it to have a subroot. 


        #we found the subroots.
        def sameTree(s, t):
            if not s and not t:
                return True #if both empty they are techaniclly true
            
            if s and t and s.val == t.val:
                return (sameTree(s.left, t.left) and sameTree(s.right, t.right))
            
            return False #do I need this right here?

        #we have the same tree so here is the answer
        if sameTree(root, subRoot):
            return True
        
        #keep searching through root tree to see if we find the same node. 
        return (self.isSubtree(root.left, subRoot) |
        self.isSubtree(root.right, subRoot)) 