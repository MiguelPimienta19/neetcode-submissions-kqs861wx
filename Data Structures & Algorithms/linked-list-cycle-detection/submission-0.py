# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        cycle = set() #only holds unique values!!

        while head: #while its not null.
            if head.val in cycle:
                return True
            cycle.add(head.val)
            head = head.next

        return False