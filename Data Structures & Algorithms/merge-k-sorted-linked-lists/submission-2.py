# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        if not lists:
            return None
        
        def mergelist(l1, l2):

            dummy = ListNode()
            cur = dummy
            while l1 and l2:
                if l1.val < l2.val: #remember we are looking for sorted
                    cur.next = l1
                    l1 = l1.next
                else:
                    cur.next = l2
                    l2 = l2.next
                
                cur = cur.next

            if l1:
                cur.next = l1
            if l2:
                cur.next = l2

            return dummy.next

        while len(lists) > 1: #need this to make sure we get all of the lists. 
            sorted_list = []
            for i in range(0, len(lists), 2):
                    l1 = lists[i]
                    l2 = lists[i + 1] if (i + 1) in range(len(lists)) else None
                    sorted_list.append(mergelist(l1,l2))

            lists = sorted_list
            
        return lists[0]
        



      
            